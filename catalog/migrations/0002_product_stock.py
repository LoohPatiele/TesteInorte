# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 23:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=5, verbose_name='Estoque'),
        ),
    ]
