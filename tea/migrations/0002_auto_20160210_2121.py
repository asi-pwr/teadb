# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tea', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teatype',
            name='name',
            field=models.CharField(max_length=1, choices=[(b'a', b'Czarna'), (b'b', b'Zielona'), (b'c', b'Czerwona'), (b'd', b'Oolong'), (b'e', b'Biala'), (b'f', b'Yerba mate'), (b'g', b'Ziolowa'), (b'h', b'Owocowe'), (b'i', b'Krzewow i kory')]),
            preserve_default=True,
        ),
    ]
