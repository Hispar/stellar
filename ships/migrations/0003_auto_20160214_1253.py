# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-14 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ships', '0002_auto_20160214_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ship',
            name='fabrication_date',
            field=models.DateField(blank=True, null=True, verbose_name='fabrication date'),
        ),
    ]
