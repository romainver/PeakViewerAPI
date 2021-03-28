# Generated by Django 3.1.7 on 2021-03-27 22:58

import django.contrib.gis.db.models.fields
from django.db import migrations
from django.contrib.gis.geos import  Point

class Migration(migrations.Migration):

    dependencies = [
        ('peaks', '0002_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='peak',
            name='coordinates',
            field=django.contrib.gis.db.models.fields.PointField(default=Point(5, 23), srid=4326),
            preserve_default=False,
        ),
    ]
