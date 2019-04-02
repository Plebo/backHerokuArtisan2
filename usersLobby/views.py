from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from usersLobby.models import UsersLobby

from usersLobby.serializers import UsersLobbySerializer


class UsersLobbyView(APIView):
    def get(self, request, format=None):
        queryset  = UsersLobby.objects.all()
        serializer = UsersLobbySerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UsersLobbySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            response = datas
            return Response(response, status=status.HTTP_201_CREATED)   
        response = serializer.errors
        return Response(response, status=404) 


class UsersLobbyEdit(APIView):
    def get_objetc(self, pk):
        try:
            return UsersLobby.objects.get(pk=pk)
        except UsersLobby.DoesNotExist:
            return "No"
    def put(self, request, pk , format=None):
        print("Hola mundo")
        Id = self.get_objetc(pk)
        serializer = UsersLobbySerializer(Id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)

class UsersLobbyList(APIView):
    def get(self, request, id, format=None):
        queryset  = UsersLobby.objects.filter(idLobby=id)
        serializer = UsersLobbySerializer(queryset, many=True)
        return Response(serializer.data)             

class UsersLobbyByUserANDLobby(APIView):
    def get(self, request, idUser, idLobby, format=None):
        queryset  = UsersLobby.objects.filter(idLobby=id, idLobby = idLobby)
        serializer = UsersLobbySerializer(queryset, many=True)
        return Response(serializer.data)