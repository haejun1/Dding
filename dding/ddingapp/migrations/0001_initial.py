# Generated by Django 4.2 on 2023-07-03 01:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gongmo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('detail', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('deadline', models.TextField()),
                ('registration_time', models.DateTimeField(auto_now_add=True)),
                ('edit_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jickgoon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=50)),
                ('detail', models.TextField()),
                ('progress', models.TextField()),
                ('registration_time', models.DateTimeField(auto_now_add=True)),
                ('edit_time', models.DateTimeField(auto_now=True)),
                ('gongmo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ddingapp.gongmo')),
                ('leader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Jickgoonjoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ddingapp.jickgoon')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='jickgoon',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ddingapp.team'),
        ),
    ]
