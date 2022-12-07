# Generated by Django 4.0 on 2022-01-17 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(default=None, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='UserroleMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=None, max_length=1000)),
                ('role_id', models.IntegerField(default=None, max_length=1000)),
            ],
        ),
    ]
