# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 20:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neurobank', '0010_auto_20170626_1509'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='created',
            new_name='registered',
        ),
    ]