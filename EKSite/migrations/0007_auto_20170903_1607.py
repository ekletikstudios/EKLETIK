# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EKSite', '0006_auto_20170830_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuredheader',
            name='description',
            field=models.TextField(blank=True, max_length=140),
        ),
    ]
