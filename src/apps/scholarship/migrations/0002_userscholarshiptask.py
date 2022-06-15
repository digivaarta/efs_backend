# Generated by Django 4.0.2 on 2022-06-14 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scholarship', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserScholarshipTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('attachment_one', models.FileField(blank=True, null=True, upload_to='scholarship/')),
                ('attachment_two', models.FileField(blank=True, null=True, upload_to='scholarship/')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('reject', 'Reject')], default='pending', max_length=100)),
                ('sub_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sch_scholarship_sub_task', to='scholarship.scholarshipsubtask')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_scholarship_task', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'sub_task')},
            },
        ),
    ]
