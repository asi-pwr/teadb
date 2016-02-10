from django.db import models

class TeaType(models.Model):
    
    tea_choices=(('a','Czarna'),('b','Zielona'),('c','Czerwona'),('d','Oolong'),('e','Biala'),('f','Yerba mate'),('g','Ziolowa'),('h','Owocowe'),('i','Krzewow i kory'),)
    name=models.CharField(max_length=1,choices=tea_choices)

class Tea(models.Model):
    name=models.ForeignKey(TeaType)
    description=models.TextField()
    region=models.CharField(max_length=100)

class Review(models.Model):
    contents=models.TextField()
    
# Create your models here.
