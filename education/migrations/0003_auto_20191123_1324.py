# Generated by Django 2.2.7 on 2019-11-23 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_education_awards'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='address',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
