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
class GetGistAPI(APIView):
    GITHUB_API = "https://api.github.com"
    url = GITHUB_API + "/gists/public"

    def get(self, request):
        res = requests.get(self.url)
        return Response(res, status=200)