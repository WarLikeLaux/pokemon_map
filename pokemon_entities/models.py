from django.db import models
from django.utils import timezone


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pokemons', null=True, blank=True)

    def __str__(self):
        return self.title


def default_disappeared_at():
    return timezone.now() + timezone.timedelta(hours=12)


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lan = models.FloatField()
    lot = models.FloatField()
    appeared_at = models.DateTimeField(default=timezone.now)
    disappeared_at = models.DateTimeField(default=default_disappeared_at)
