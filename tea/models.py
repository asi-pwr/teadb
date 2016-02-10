from django.db import models

class TeaType(models.Model):
    name=models.CharField(max_length=100)

class Tea(models.Model):
    name=models.ForeignKey(TeaType)
    description=models.TextField()
    region=models.CharField(max_length=100)

class Review(models.Model):
    contents=models.TextField()
    
# Create your models here.
