from django.db import models
# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    standard=models.CharField(max_length=4)
    marks=models.IntegerField()
    
