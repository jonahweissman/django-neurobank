# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neurobank', '0008_auto_20170626_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='sha1',
            field=models.CharField(blank=True, help_text='specify only for resources whose contents must not change (i.e., sources)', max_length=40, null=True, unique=True),
        ),
    ]
