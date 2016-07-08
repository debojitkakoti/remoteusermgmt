# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 10:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='userid',
        ),
        migrations.AddField(
            model_name='users',
            name='projid',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]