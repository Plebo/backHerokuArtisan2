from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from words.models import Words

from words.serializers import WordsSerializer

class WordsLobbyView(APIView):
    def get(self, request, format=None):
        queryset  = Words.objects.all()
        serializer = WordsSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WordsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            response = datas
            return Response(response, status=status.HTTP_201_CREATED)   
        response = serializer.errors
        return Response(response, status=404)

class WordsLobbyById(APIView):
    def get(self, request, pk, format=None):
        queryset  = Words.objects.filter(pk=pk)
        serializer = WordsSerializer(queryset, many=True)
        return Response(serializer.data)
# Create your views here.
