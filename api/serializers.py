from dataclasses import field
from rest_framework import serializers
from .models import DatasetOne,DatasetTwo

class DatasetOneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DatasetOne
        fields = ('id','url','name','email','phone_number','Idnumber','DateOfBirth')

