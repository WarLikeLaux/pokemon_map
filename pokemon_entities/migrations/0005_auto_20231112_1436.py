from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0004_auto_20231112_1419'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='lan',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='lot',
            new_name='lon',
        ),
    ]
