# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-09 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20170509_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinfo',
            name='logo',
            field=models.FilePathField(),
        ),
    ]
