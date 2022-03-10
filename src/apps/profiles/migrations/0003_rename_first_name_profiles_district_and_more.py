# Generated by Django 4.0.2 on 2022-03-10 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profiles_full_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profiles',
            old_name='first_name',
            new_name='district',
        ),
        migrations.RenameField(
            model_name='profiles',
            old_name='last_name',
            new_name='pincode',
        ),
        migrations.AddField(
            model_name='profiles',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profiles',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
