# Generated by Django 2.1.7 on 2019-04-21 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0009_auto_20190417_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='personal_website',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]