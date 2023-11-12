from django.db import models
from django.utils import timezone


class Pokemon(models.Model):
    title = models.CharField("Название", max_length=200)
    title_en = models.CharField("Название (англ.)", max_length=200, default='')
    title_jp = models.CharField("Название (япон.)", max_length=200, default='')
    image = models.ImageField("Изображение", upload_to='pokemons', null=True, blank=True)
    description = models.TextField("Описание", default='')
    previous_evolution = models.ForeignKey('self', verbose_name="Предыдущая эволюция", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


def default_disappeared_at():
    return timezone.now() + timezone.timedelta(hours=12)


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name="Покемон", on_delete=models.CASCADE)
    lat = models.FloatField("Широта")
    lon = models.FloatField("Долгота")
    appeared_at = models.DateTimeField("Время появления", default=timezone.now)
    disappeared_at = models.DateTimeField("Время исчезновения", default=default_disappeared_at)
    level = models.IntegerField("Уровень", default=1)
    health = models.IntegerField("Здоровье", default=100)
    strength = models.IntegerField("Сила", default=10)
    defence = models.IntegerField("Защита", default=10)
    stamina = models.IntegerField("Выносливость", default=10)
