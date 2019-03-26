from django.db import models
from django.contrib.auth.models import User
from lobby.models import Lobby
# Create your models here.
class UsersLobby(models.Model):
    idUser = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    idLobby = models.ForeignKey(Lobby,null=True, on_delete=models.CASCADE)  