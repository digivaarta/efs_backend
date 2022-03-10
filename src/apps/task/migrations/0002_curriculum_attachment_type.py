# Generated by Django 4.0.2 on 2022-03-10 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curriculum',
            name='attachment_type',
            field=models.CharField(choices=[('video', 'Video'), ('image', 'Image'), ('text', 'Text')], default='image', max_length=300),
        ),
    ]