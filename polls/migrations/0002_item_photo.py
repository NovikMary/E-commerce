# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='photo',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
