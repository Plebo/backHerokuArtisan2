from django.db import models
from django.contrib.auth.models import User
from lobby.models import Lobby
# Create your models here.
class Message(models.Model):
    idUsers = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()  
    idLobby = models.ForeignKey(Lobby, on_delete=models.CASCADE)