# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='trnsaction_type',
            field=models.CharField(blank=True, choices=[('General', 'General'), ('POS', 'POS')], max_length=32),
        ),
    ]
