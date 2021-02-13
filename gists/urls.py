from django.conf.urls import url, include
from django.urls import path
from gists.views import GetGistAPI

app_name = "gists"

urlpatterns = [
    path('getGists/', GetGistAPI.as_view()),
]