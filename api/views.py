from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import DatasetOneSerializer
# Create your views here.

class DatasetOneView(viewsets.ModelViewSet):
    queryset = DatasetOne.objects.all()
    serializer_class = DatasetOneSerializer
