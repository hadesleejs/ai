# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-07-06 03:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IMG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='image?default.png', max_length=500, upload_to='/img/%Y/%m')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '\u7528\u6237\u4e0a\u4f20',
                'verbose_name_plural': '\u7528\u6237\u4e0a\u4f20',
            },
        ),
    ]
