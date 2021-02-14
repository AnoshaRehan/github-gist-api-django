from rest_framework.renderers import TemplateHTMLRenderer
import requests
from rest_framework.views import APIView
from rest_framework.response import Response

import json

# Create your views here.
GITHUB_API = "https://api.github.com"

class GetPublicGistAPI(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'gists_results.html'

    url = GITHUB_API + "/gists/public"
    def get(self, request):
        res = requests.get(self.url)
        data = json.loads(res.text)
        return Response({'response': data})

class GetUserGistsAPI(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'search_results.html'
    def get(self, request):
        url = GITHUB_API + "/users/{}/gists".format(request.GET['username'])
        res = requests.get(url)
        return Response({'response': res})


class GetForksAPI(APIView):

    def get(self, request):
        url = GITHUB_API + "/gists/{}/forks".format(request.GET['gist_id'])
        res = requests.get(url)
        user_avatar = {}
        data = json.loads(res.text) # All forks
        last_three = data[-3:] # Recently forked
        for i in range(len(last_three)):
            avatar = last_three[i]['owner']['avatar_url']
            username = last_three[i]['owner']['login']
            if username not in user_avatar:
                user_avatar[username] = avatar
        return Response(user_avatar, status=200)


class GetGistContentAPI(APIView):

    def get(self, request, id):
        gist_id = id
        url = GITHUB_API + "/gists/{}".format(gist_id)
        resp = requests.get(url)
        data = json.loads(resp.text)
        file = list(data['files'].items())[0]
        content = file[-1]['content']
        print(content)

        return Response(content, status=200)
