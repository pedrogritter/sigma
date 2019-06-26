# Generated by Django 2.1.7 on 2019-06-25 23:35

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0012_profile_chairs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='chairs',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None),
        ),
    ]
