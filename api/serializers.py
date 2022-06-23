from dataclasses import field
from rest_framework import serializers
from .models import DatasetOne,DatasetTwo

class DatasetOneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DatasetOne
        fields = ('id','url','name','email','phone_number','Idnumber','DateOfBirth')


class DatasetTwoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DatasetTwo
        fields = ('id','url','name','phone_number','Idnumber','DateOfBirth')
