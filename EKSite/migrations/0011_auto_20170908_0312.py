# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 03:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EKSite', '0010_person_board_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioproject',
            name='description',
            field=models.TextField(),
        ),
    ]
