# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-09-30 11:47
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ThakkarbappayojanaMokhadaCulvert10',
            fields=[
                ('fid_1', models.AutoField(primary_key=True, serialize=False)),
                ('the_geom', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('fid', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, db_column=b'Name', max_length=254, null=True)),
                ('panchayat_field', models.CharField(blank=True, db_column=b'Panchayat_', max_length=254, null=True)),
                ('village_na', models.CharField(blank=True, db_column=b'Village_Na', max_length=254, null=True)),
                ('habitation', models.CharField(blank=True, db_column=b'Habitation', max_length=254, null=True)),
                ('budget', models.CharField(blank=True, db_column=b'Budget', max_length=254, null=True)),
                ('sanction_y', models.CharField(blank=True, db_column=b'Sanction_y', max_length=254, null=True)),
                ('work_type', models.CharField(blank=True, db_column=b'Work_type', max_length=254, null=True)),
                ('work_name', models.CharField(blank=True, db_column=b'Work_Name', max_length=254, null=True)),
                ('width', models.CharField(blank=True, db_column=b'Width', max_length=254, null=True)),
                ('no_of_pipe', models.CharField(blank=True, db_column=b'No_of_Pipe', max_length=254, null=True)),
                ('final_asse', models.CharField(blank=True, db_column=b'Final_Asse', max_length=254, null=True)),
                ('remark', models.CharField(blank=True, db_column=b'Remark', max_length=254, null=True)),
            ],
            options={
                'db_table': 'ThakkarBappaYojana_Mokhada_Culvert_1_0',
                'managed': False,
            },
        ),
    ]
