# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-09-02 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_auto_20180902_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='shortcode',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]