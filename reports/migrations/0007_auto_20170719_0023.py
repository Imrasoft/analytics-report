# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-19 00:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_remove_campaignevent_campaign_event_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaignevent',
            name='flow',
            field=models.CharField(max_length=200),
        ),
    ]