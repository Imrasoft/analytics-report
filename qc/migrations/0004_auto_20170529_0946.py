# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 06:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qc', '0003_auto_20170529_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='modified_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='sent_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
