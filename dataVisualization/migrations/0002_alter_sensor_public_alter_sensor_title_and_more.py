# Generated by Django 5.0.1 on 2024-01-07 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataVisualization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='public',
            field=models.BooleanField(default=True, verbose_name='¿?Publicado'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='title',
            field=models.CharField(default='Sin título', max_length=159, null=True, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='value',
            field=models.FloatField(default=None, null=True, verbose_name='Valor'),
        ),
    ]
