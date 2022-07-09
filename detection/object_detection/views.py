from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from.find_object import *
from .serializer import object_detectionSerializer
# Create your views here.
class findlist(APIView):
    
    def get(self):
        obj=obj_list()
        serializer=object_detectionSerializer(arr,many=True)
        return Response(serializer.data)

    def post(self):
        pass