from django.conf.urls import url, include
from django.urls import path
from gists.views import GetPublicGistAPI, GetUserGistsAPI, GetForksAPI, GetGistContentAPI

app_name = "gists"

urlpatterns = [
    path('getGists/', GetPublicGistAPI.as_view(), name='gists_results'),
    url(r'^getUserGist/$', GetUserGistsAPI.as_view(), name='search_results'),
    url(r'^getForks/$', GetForksAPI.as_view()),
    path('getGistContent/<str:id>', GetGistContentAPI.as_view())
]