# Generated by Django 3.2.22 on 2023-11-12 14:14

from django.db import migrations, models
import django.utils.timezone
import pokemon_entities.models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0002_auto_20231112_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(),
        ),
    ]
