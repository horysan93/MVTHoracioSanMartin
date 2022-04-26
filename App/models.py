from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length = 40)
    edad = models.IntegerField()
    vinculo = models.CharField(max_length = 40)
    nacimiento = models.DateField()

class Mascota(models.Model):
    nombre = models.CharField(max_length = 40)
    especie = models.CharField(max_length = 40)



