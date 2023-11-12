from django.db import models
from django.utils import timezone


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, default='')
    title_jp = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='pokemons', null=True, blank=True)
    description = models.TextField(default='')

    def __str__(self):
        return self.title


def default_disappeared_at():
    return timezone.now() + timezone.timedelta(hours=12)


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(default=timezone.now)
    disappeared_at = models.DateTimeField(default=default_disappeared_at)
    level = models.IntegerField(default=1)
    health = models.IntegerField(default=100)
    strength = models.IntegerField(default=10)
    defence = models.IntegerField(default=10)
    stamina = models.IntegerField(default=10)
