# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-24 11:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store_products', '0009_auto_20170823_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 24, 11, 23, 5, 421845, tzinfo=utc)),
        ),
    ]