from django.db import models

# Create your models here.

class familiar(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fecha_nacimiento = models.CharField(max_length=40)
    dni = models.IntegerField()

