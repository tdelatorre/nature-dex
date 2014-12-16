# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Specimen',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('ext_ref', models.CharField(max_length=50, unique=True, verbose_name='External reference')),
                ('specimen_image', models.ImageField(blank=True, default=None, upload_to='images', null=True)),
                ('track_image', models.ImageField(blank=True, default=None, upload_to='images', null=True)),
                ('leaf_image', models.ImageField(blank=True, default=None, upload_to='images', null=True)),
                ('common_name', models.CharField(blank=True, max_length=255, verbose_name='Common name')),
                ('scientific_name', models.CharField(blank=True, max_length=255, verbose_name='Scientific name')),
                ('group', models.CharField(blank=True, max_length=255, verbose_name='Group')),
                ('genus', models.CharField(blank=True, max_length=255, verbose_name='Genus')),
                ('species', models.CharField(blank=True, max_length=255, verbose_name='Species')),
                ('kingdom', models.CharField(blank=True, max_length=255, verbose_name='Kingdom')),
                ('division', models.CharField(blank=True, max_length=255, verbose_name='Division')),
                ('kind', models.CharField(blank=True, max_length=255, verbose_name='Kind (Class)')),
                ('order', models.CharField(blank=True, max_length=255, verbose_name='Order')),
                ('family', models.CharField(blank=True, max_length=255, verbose_name='Family')),
                ('identification', models.TextField(blank=True, verbose_name='Identification')),
                ('status', models.TextField(blank=True, verbose_name='Status')),
                ('distribution', models.TextField(blank=True, verbose_name='Distribution')),
                ('habitat', models.TextField(blank=True, verbose_name='Habitat')),
                ('diet', models.TextField(blank=True, verbose_name='Diet')),
                ('reproduction', models.TextField(blank=True, verbose_name='Reproduction')),
                ('interactions', models.TextField(blank=True, verbose_name='Interactions')),
                ('behavior', models.TextField(blank=True, verbose_name='Behavior')),
            ],
            options={
                'verbose_name_plural': 'Specimenes',
                'verbose_name': 'Specimen',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('ext_ref', models.CharField(max_length=10, unique=True, verbose_name='External reference')),
                ('marine', models.BooleanField(default=False, verbose_name='Marine')),
                ('mpoly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Zones',
                'verbose_name': 'Zone',
            },
            bases=(models.Model,),
        ),
    ]
