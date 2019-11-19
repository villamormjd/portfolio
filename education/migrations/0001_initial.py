# Generated by Django 2.2.7 on 2019-11-19 08:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=200)),
                ('course', models.CharField(blank=True, max_length=250)),
                ('address', models.CharField(max_length=500)),
                ('start_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('end_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
