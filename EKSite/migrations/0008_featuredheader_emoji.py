# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EKSite', '0007_auto_20170903_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuredheader',
            name='emoji',
            field=models.BooleanField(default=False),
        ),
    ]
