# Generated by Django 4.0.2 on 2022-02-08 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_support', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('ticket_no', django_extensions.db.fields.RandomCharField(blank=True, editable=False, include_digits=False, length=12, lowercase=True)),
                ('status', models.CharField(choices=[('open', 'Open'), ('closed', 'Closed')], default='open', max_length=100)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('support', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='support_ticket', to='support.support')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_ticket', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
