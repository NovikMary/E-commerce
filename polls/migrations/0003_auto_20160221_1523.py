# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 15:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_item_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='name_of_item',
            new_name='name',
        ),
    ]