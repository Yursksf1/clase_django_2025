from django.db import models

# Create your models here.


class TimeLine(models.Model):
    year = models.PositiveSmallIntegerField()
    name = models.CharField(
        max_length=500,
        verbose_name="Nombre"
    )
    description = models.TextField(
        verbose_name="Descripcion"
    )    
    
    def __str__(self):
        return "{}-{}".format(self.year, self.name)