# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-06 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0002_auto_20170606_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='estado',
            field=models.CharField(choices=[('Por aprobar', 'Por aprobar'), ('Aprobado', 'Aprobado'), ('Cerrado', 'Cerrado'), ('No es bug', 'No es bug'), ('No arreglado', 'No arreglado')], default='Por aprobar', max_length=30),
        ),
    ]