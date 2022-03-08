# Generated by Django 4.0.2 on 2022-03-08 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('utility', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaContentCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=600, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mcc_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='metacontent',
            name='meta_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_mcc', to='utility.metacontentcategory'),
            preserve_default=False,
        ),
    ]
