# Generated by Django 5.0.3 on 2024-06-05 18:00

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
            name='EventComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('eventId', models.IntegerField()),
                ('commentData', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='EventParticipation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('eventId', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('participation', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('shortDescription', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=2000)),
                ('status', models.CharField(choices=[('SOCIAL', 'SOCIAL'), ('WEBINARY', 'WEBINARY'), ('MEETING', 'MEETING'), ('ONLINE MEETING', 'ONLINE MEETING'), ('OTHER', 'OTHER')], default='OTHER', max_length=30)),
                ('country', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=75)),
                ('address', models.CharField(max_length=200)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
