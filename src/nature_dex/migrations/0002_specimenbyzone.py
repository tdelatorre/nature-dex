# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nature_dex', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecimenByZone',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('specimen', models.ForeignKey(verbose_name='Specimen', to='nature_dex.Specimen')),
                ('zone', models.ForeignKey(verbose_name='Zone', to='nature_dex.Zone')),
            ],
            options={
                'verbose_name': 'Specimen by zone',
                'verbose_name_plural': 'Specimenes by zones',
            },
            bases=(models.Model,),
        ),
    ]
