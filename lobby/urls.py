from django.conf.urls import include
from django.conf.urls import re_path
from lobby.views import *

urlpatterns=[
    re_path(r'^$',LobbyView.as_view(), name='lobby'),
    re_path(r'^edit/(?P<pk>\d+)$', LobbyList.as_view(), name='lobbyEdit')
]