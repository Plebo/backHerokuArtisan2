from usersLobby.models import UsersLobby
from rest_framework import serializers

class UsersLobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersLobby
        fields = ('__all__')