# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 04:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codescanner', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='uuid',
        ),
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]