# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-13 09:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20160221_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('comments_Item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Item')),
            ],
            options={
                'db_table': 'comments',
            },
        ),
    ]
