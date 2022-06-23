from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import DatasetOneSerializer,DatasetTwoSerializer
# Create your views here.

class DatasetOneView(viewsets.ModelViewSet):
    queryset = DatasetOne.objects.all()
    serializer_class = DatasetOneSerializer


class DatasetTwoView(viewsets.ModelViewSet):
    queryset = DatasetTwo.objects.all()
    serializer_class = DatasetTwoSerializer