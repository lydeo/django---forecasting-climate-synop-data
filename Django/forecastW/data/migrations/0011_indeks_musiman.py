# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-19 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0010_remove_data_klimat_kec_rata_angin1'),
    ]

    operations = [
        migrations.CreateModel(
            name='indeks_musiman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bulan', models.CharField(max_length=40)),
                ('temp_rata2', models.FloatField(null=True)),
                ('temp_max', models.FloatField(null=True)),
                ('temp_min', models.FloatField(null=True)),
                ('curah_hujan', models.FloatField(null=True)),
                ('penyinaran_matahari', models.FloatField(null=True)),
                ('tekanan_udara', models.FloatField(null=True)),
                ('kelembaban', models.FloatField(null=True)),
                ('kec_rata_angin', models.FloatField(null=True)),
            ],
        ),
    ]
