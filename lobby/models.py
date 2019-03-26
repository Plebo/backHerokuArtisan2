from django.db import models

# Create your models here.
class Lobby(models.Model):
    name = models.CharField(max_length=50, null=True)
    playersCount = models.IntegerField(null=True)  
    