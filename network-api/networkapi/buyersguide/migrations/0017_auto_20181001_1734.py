# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-01 17:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyersguide', '0016_auto_20181001_1733'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='has_moz_approval',
            new_name='meets_minimum_security_standards',
        ),
    ]
