# Generated by Django 4.2.11 on 2024-05-28 14:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_eventparticipation_date_eventparticipation_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventcomments',
            name='commentData',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]