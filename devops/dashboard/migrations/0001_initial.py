# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-19 03:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='idc名称')),
                ('address', models.CharField(default='', max_length=200, verbose_name='idc的地址')),
                ('phone', models.CharField(max_length=20, null=True, verbose_name='idc的联系电话')),
                ('user', models.CharField(max_length=32, null=True, verbose_name='idc的联系人')),
            ],
        ),
    ]
