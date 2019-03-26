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

# class UsersLobbyList(APIView):
#        def get(self, pk, request, format=None):
#         queryset  = UsersLobby.objects.filter(idLobby=pk)
#         serializer = UsersLobbySerializer(queryset, many=True)
#         return Response(serializer.data)          
    # def put(self, request, pk ):
    #     usersLobby = UsersLobby.objects.get(pk=pk)
    #     UsersLobby_json = UsersLobbySerializer(usersLobby, data=request.data)
    #     if UsersLobby_json.is_valid():
    #         UsersLobby_json.save()
    #         return Response(UsersLobby_json.data, status=201)
    #     return Response(UsersLobby_json.errors, status=400)    
