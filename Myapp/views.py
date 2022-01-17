from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Myapp.serializer import traineeSerializer
from . models import trainee
from . serializer import traineeSerializer

class traineelist(APIView):

    def get(self, request):
        trainee1 = trainee.objects.all()
        serializer = traineeSerializer(trainee1, many = True)
        return Response(serializer.data)
