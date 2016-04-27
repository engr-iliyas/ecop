# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-14 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimefiles', '0002_auto_20160414_2010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='description',
            new_name='content',
        ),
        migrations.AlterField(
            model_name='complaint',
            name='dateofcomplaint',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]