# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-15 08:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crimefiles', '0006_fir_complaintid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fir',
            name='complaintid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='crimefiles.Complaint'),
        ),
    ]
