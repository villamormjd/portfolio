# Generated by Django 2.2.7 on 2019-11-23 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='awards',
            field=models.TextField(blank=True),
        ),
    ]
