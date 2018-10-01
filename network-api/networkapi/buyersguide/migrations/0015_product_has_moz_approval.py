# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-01 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyersguide', '0014_auto_20180928_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_moz_approval',
            field=models.NullBooleanField(help_text='Does this product bear the Mozilla seal of approval?'),
        ),
    ]