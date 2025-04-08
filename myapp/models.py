from django.db import models

# Create your models here.
class Park(models.Model):
    name = models.CharField(
        max_length=500,
        verbose_name="Nombre Parque"
    )
    description = models.TextField(
        verbose_name="Descripcion Parque"
    )
