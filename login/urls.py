from django.urls import re_path
from login.views import CustomAuthToken

urlpatterns = [
     re_path(r'^', CustomAuthToken.as_view()),
]
