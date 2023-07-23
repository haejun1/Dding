# Generated by Django 4.2 on 2023-07-23 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ddingapp', '0011_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='message',
        ),
        migrations.AddField(
            model_name='notification',
            name='jickgoon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ddingapp.jickgoon'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
