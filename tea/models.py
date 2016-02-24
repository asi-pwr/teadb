from django.db import models

class TeaType(models.Model):
    name=models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Tea(models.Model):
    name=models.ForeignKey(TeaType)
    description=models.TextField()
    region=models.CharField(max_length=100)

    def __str__(self):
        return self.name.name


class Review(models.Model):
    contents=models.TextField()
    
