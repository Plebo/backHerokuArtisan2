from lobby.models import Lobby
from rest_framework import serializers

class lobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lobby
        fields = ('__all__')