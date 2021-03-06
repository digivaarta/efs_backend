# Generated by Django 4.0.2 on 2022-05-26 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pledge', '0002_userpledge_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='pledge',
            name='cover_image_en',
            field=models.ImageField(blank=True, null=True, upload_to='pledge/'),
        ),
        migrations.AddField(
            model_name='pledge',
            name='cover_image_hi',
            field=models.ImageField(blank=True, null=True, upload_to='pledge/'),
        ),
        migrations.AddField(
            model_name='pledge',
            name='title_en',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='pledge',
            name='title_hi',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='pledgedata',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='pledgedata',
            name='content_hi',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='pledgedata',
            name='cover_image_en',
            field=models.ImageField(blank=True, null=True, upload_to='pledge/'),
        ),
        migrations.AddField(
            model_name='pledgedata',
            name='cover_image_hi',
            field=models.ImageField(blank=True, null=True, upload_to='pledge/'),
        ),
        migrations.AddField(
            model_name='pledgedata',
            name='title_en',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='pledgedata',
            name='title_hi',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
