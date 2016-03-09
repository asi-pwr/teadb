from django.db import models

class TeaType(models.Model):
    tea_type_choices=(
        ('a', 'Czarna'),
        ('b', 'Zielona'),
        ('c', 'Czerwona'),
        ('d', 'Oolong'),
        ('e', 'Biala'),
        ('f', 'Yerba mate'),
        ('g', 'Ziolowa'),
        ('h', 'Owocowe'),
        ('i', 'Krzewow i kory'),
        ('j', 'Rooibos'),
        ('k', "Pu-Erh"),
    )
    tea_type=models.CharField(max_length=1, choices=tea_type_choices)

    def __str__(self):
        return "%s" % self.get_tea_type_display()

class Tea(models.Model):
    name=models.CharField(max_length=50)
    type=models.ForeignKey(TeaType)
    description=models.TextField()
    region=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Review(models.Model):
    reviewed_tea=models.ForeignKey(Tea)
    content=models.TextField()
    author=models.CharField(max_length=50)