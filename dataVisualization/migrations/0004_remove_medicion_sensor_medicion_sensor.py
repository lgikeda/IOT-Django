# Generated by Django 5.0.1 on 2024-01-10 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataVisualization', '0003_medicion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicion',
            name='sensor',
        ),
        migrations.AddField(
            model_name='medicion',
            name='sensor',
            field=models.ManyToManyField(related_name='mediciones', to='dataVisualization.sensor'),
        ),
    ]
