from django.conf.urls import include
from django.conf.urls import re_path
from usersLobby.views import *

urlpatterns=[
    re_path(r'^$',UsersLobbyView.as_view(), name='UsersLobby'),
    re_path(r'^edit/(?P<pk>\d+)$', UsersLobbyEdit.as_view(), name='UsersLobby'),
    re_path(r'^data/list/(?P<id>\d+)$', UsersLobbyList.as_view(), name='UsersLobby1'),
    re_path(r'^data/photo/(?P<idUser>\d+)/(?P<idLobby>\d+)$', UsersLobbyByUserANDLobby.as_view(), name='UsersLobbyPhoto')
]