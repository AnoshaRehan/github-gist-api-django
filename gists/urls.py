from django.conf.urls import url, include
from django.urls import path
from gists.views import GetPublicGistAPI, GetUserGistsAPI

app_name = "gists"

urlpatterns = [
    path('getGists/', GetPublicGistAPI.as_view()),
    url(r'^getUserGist/$', GetUserGistsAPI.as_view())
]