from django.db import models


class Pokemon(models.Model):
    title = models.CharField("Название", max_length=200)
    title_en = models.CharField("Название (англ.)", max_length=200, blank=True)
    title_jp = models.CharField("Название (япон.)", max_length=200, blank=True)
    image = models.ImageField("Изображение", upload_to='pokemons')
    description = models.TextField("Описание", blank=True)
    previous_evolution = models.ForeignKey(
        'self',
        verbose_name="Предыдущая эволюция",
        related_name="next_evolutions",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        verbose_name="Покемон",
        related_name="entities",
        on_delete=models.CASCADE
    )
    lat = models.FloatField("Широта")
    lon = models.FloatField("Долгота")
    appeared_at = models.DateTimeField("Время появления")
    disappeared_at = models.DateTimeField("Время исчезновения")
    level = models.IntegerField("Уровень")
    health = models.IntegerField("Здоровье")
    strength = models.IntegerField("Сила")
    defence = models.IntegerField("Защита")
    stamina = models.IntegerField("Выносливость")

    def __str__(self):
        return f"{self.pokemon.title} (lvl {self.level}) on {self.lat}, {self.lon}"
