# Generated by Django 5.0.6 on 2024-07-01 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
