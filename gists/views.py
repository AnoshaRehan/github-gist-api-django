from django.shortcuts import render
from django.shortcuts import render
import requests
import time
from django.db import connection
from functools import wraps
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import logging
from requests import get
import json

# Create your views here.
GITHUB_API = "https://api.github.com"

class GetPublicGistAPI(APIView):
    url = GITHUB_API + "/gists/public"

    def get(self, request):
        res = requests.get(self.url)
        return Response(res, status=200)

class GetUserGistsAPI(APIView):

    def get(self, request):
        url = GITHUB_API + "/users/{}/gists".format(request.GET['username'])
        res = requests.get(url)
        return Response(res, status=200)

class GetForksAPI(APIView):

    def get(self, request):
        url = GITHUB_API + "/gists/{}/forks".format(request.GET['gist_id'])
        res = requests.get(url)
        user_avatar = {}
        data = json.loads(res.text)
        for i in range(len(data)):
            avatar = data[i]['owner']['avatar_url']
            username = data[i]['owner']['login']
            if username not in user_avatar:
                user_avatar[username] = avatar
        return Response(user_avatar, status=200)
