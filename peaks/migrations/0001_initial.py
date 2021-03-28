# Generated by Django 3.1.7 on 2021-03-26 17:57

from django.db import migrations, models
from django.contrib.postgres.operations import CreateExtension

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
    CreateExtension('postgis'),
        migrations.CreateModel(
            name='Peak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peak_name', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('altitude', models.FloatField()),
            ],
        ),
    ]