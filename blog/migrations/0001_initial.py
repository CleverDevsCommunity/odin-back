# Generated by Django 5.1 on 2024-11-01 07:07

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_count', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=100, null=True)),
                ('time_created', models.TimeField(auto_now=True)),
                ('description', models.CharField(max_length=250, null=True)),
                ('body', models.TextField(max_length=10000)),
                ('image', models.ImageField(default='pics/placeholder.png', null=True, upload_to='pics/')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]