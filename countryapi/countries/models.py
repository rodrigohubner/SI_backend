from django.db import models


class Continent(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    


class Country(models.Model):
    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'countries'