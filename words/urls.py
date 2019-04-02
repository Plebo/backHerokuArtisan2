from django.conf.urls import include
from django.conf.urls import re_path
from words.views import *

urlpatterns=[
    re_path(r'^$', WordsLobbyView.as_view(), name='Words'),
    re_path(r'^data/wordById/(?P<pk>\d+)$', WordsLobbyById.as_view(), name='WordById')
]