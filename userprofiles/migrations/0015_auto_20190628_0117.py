# Generated by Django 2.2.2 on 2019-06-28 01:17

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0014_auto_20190627_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='chairs',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=4), blank=True, default=list, null=True, size=None),
        ),
    ]