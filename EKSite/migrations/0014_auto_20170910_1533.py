# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-10 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EKSite', '0013_auto_20170908_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioproject',
            name='publishedDate',
            field=models.DateTimeField(),
        ),
    ]
