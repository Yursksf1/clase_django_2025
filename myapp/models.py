from django.db import models

# Create your models here.
class Park(models.Model):
    CITY_CHOICES = [
        ("BUC", "Bucaramanga"),
        ("GRN", "Giron"),
        ("FLD", "Floridablanca"),
        ("PDC", "Piedecuesta"),
    ]
    name = models.CharField(
        max_length=500,
        verbose_name="Nombre Parque"
    )
    description = models.TextField(
        verbose_name="Descripcion Parque"
    )

    city = models.CharField(max_length=3, choices=CITY_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name

class Historico_Poblacion(models.Model):
    year = models.PositiveSmallIntegerField()
    poblation = models.PositiveIntegerField()
    
    def __str__(self):
        return "{}-{}".format(self.year, self.poblation)