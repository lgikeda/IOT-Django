# Generated by Django 5.0.1 on 2024-01-10 19:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataVisualization', '0002_alter_sensor_public_alter_sensor_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mediciones', to='dataVisualization.sensor')),
            ],
        ),
    ]
