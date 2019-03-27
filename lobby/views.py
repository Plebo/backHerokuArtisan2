from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from lobby.models import Lobby

from .serializers import lobbySerializer

class LobbyView(APIView):
    def get(self, request, format=None):
        queryset  = Lobby.objects.all()
        serializer = lobbySerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = lobbySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            response = datas
            return Response(response, status=status.HTTP_201_CREATED)   
        response = serializer.errors
        
        return Response(response, status=404) 

class LobbyEdit(APIView):

    def get_objetc(self, pk):
        try:
            return Lobby.objects.get(pk=pk)
        except Lobby.DoesNotExist:
            return "No"
    def put(self, request, pk , format=None):
        print("Hola mundo")
        Id = self.get_objetc(pk)
        serializer = lobbySerializer(Id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        # Id = lobbySerializer(Id)
        # return Response(Id.data)


class LobbyList(APIView):
    def get(self, request, id, format=None):
        queryset  = Lobby.objects.filter(pk=id)
        serializer = lobbySerializer(queryset, many=True)
        return Response(serializer.data) 