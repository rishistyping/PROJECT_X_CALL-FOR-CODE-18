# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-13 17:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('evidence', '0013_auto_20180813_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='evidence',
            name='publication_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='evidence',
            name='slug',
            field=models.SlugField(allow_unicode=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]