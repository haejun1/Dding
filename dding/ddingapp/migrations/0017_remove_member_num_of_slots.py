# Generated by Django 4.2 on 2023-07-26 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ddingapp', '0016_team_design_capacity_team_dev_capacity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='num_of_slots',
        ),
    ]
