from django.db import models

# Create your models here.
class DatasetOne(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=50)
    Idnumber = models.CharField(max_length=50)
    DateOfBirth = models.DateField(max_length=8)

    def __str__(self):
        return self.name



class DatasetTwo(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50)
    Idnumber = models.CharField(max_length=50)
    DateOfBirth = models.DateField(max_length=8)



    def __str__(self):
        return self.name
