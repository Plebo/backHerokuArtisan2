from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from message.models import Message

from message.serializers import messageSerializer


class MessageView(APIView):
    def get(self, request, format=None):
        print("GET")
        queryset  = Message.objects.all()
        serializer = messageSerializer(queryset, many=True)
        return Response(serializer.data)
    

    def post(self, request, format=None):
        serializer = messageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            response = datas
            return Response(response, status=status.HTTP_201_CREATED)   
        response = serializer.errors
        return Response(response, status=404)    