# Generated by Django 4.2 on 2023-07-16 06:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ddingapp', '0008_jickgoon_member_team_jickgoons'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
