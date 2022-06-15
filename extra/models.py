from django.db import models

# Create your models here.

class Carusel(models.Model):
    titel = models.CharField("Nomi", max_length=200)
    image = models.ImageField("Rasim", upload_to='carusel/')

    class Meta:
        verbose_name = "Carusel"
        verbose_name_plural = "Carusel"

    def __str__(self):
        return self.titel