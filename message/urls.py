from django.conf.urls import include
from django.conf.urls import re_path
from message.views import MessageView

urlpatterns=[
    re_path(r'^',MessageView.as_view(), name='messages'),
]