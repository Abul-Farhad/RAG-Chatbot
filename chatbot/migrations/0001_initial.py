# Generated by Django 5.2.4 on 2025-07-08 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMemory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=255, unique=True)),
                ('state_json', models.JSONField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
