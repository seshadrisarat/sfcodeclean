# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 07:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codescanner', '0002_auto_20171124_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='email',
            field=models.EmailField(default='ben@edwards.nz', max_length=254),
            preserve_default=False,
        ),
    ]