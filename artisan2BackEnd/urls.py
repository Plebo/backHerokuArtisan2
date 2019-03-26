"""artisan2BackEnd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include, url
from rest_framework import routers, serializers, viewsets

from django.contrib.auth.models import User


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username','password')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer     

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^artisan2/v1/', include(router.urls)),
    re_path(r'^artisan2/v1/login/', include('login.urls')),
    re_path(r'^artisan2/v1/message/', include('message.urls')),
    #re_path(r'^artisan2/v1/', include('users.urls')),
    re_path(r'^artisan2/v1/usersLobby/', include('usersLobby.urls')),
    re_path(r'^artisan2/v1/lobby/', include('lobby.urls')),
    re_path(r'^rest-auth/', include('rest_auth.urls')),
    re_path(r'^artisan2/v1/registro/', include('rest_auth.registration.urls'))
    #url(r'^rest-auth/', include('rest_auth.urls')),
]
