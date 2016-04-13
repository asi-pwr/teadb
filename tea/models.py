from django.db import models

class TeaType(models.Model):
    tea_type = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % self.tea_type

class Tea(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(TeaType)
    description = models.TextField()
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Review(models.Model):
    reviewed_tea = models.ForeignKey(Tea)
    content = models.TextField()
    author = models.CharField(max_length=50)