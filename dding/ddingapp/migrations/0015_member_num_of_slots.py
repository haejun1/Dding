# Generated by Django 4.2 on 2023-07-26 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddingapp', '0014_alter_notification_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='num_of_slots',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
