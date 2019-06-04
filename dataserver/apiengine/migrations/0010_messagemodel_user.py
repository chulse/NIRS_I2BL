# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-04 18:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apiengine', '0009_auto_20190523_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagemodel',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]