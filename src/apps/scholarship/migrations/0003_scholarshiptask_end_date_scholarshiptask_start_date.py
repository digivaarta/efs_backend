# Generated by Django 4.0.2 on 2022-08-22 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0002_userscholarshiptask'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarshiptask',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scholarshiptask',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]