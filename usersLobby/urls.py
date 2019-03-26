from django.conf.urls import include
from django.conf.urls import re_path
from usersLobby.views import *

urlpatterns=[
    re_path(r'^$',UsersLobbyView.as_view(), name='UsersLobby'),
    re_path(r'^edit/(?P<pk>\d+)$', UsersLobbyEdit.as_view(), name='UsersLobby'),
    re_path(r'^data/list/(?P<pk>\d+)$', UsersLobbyList.as_view(), name='UsersLobby1')
]