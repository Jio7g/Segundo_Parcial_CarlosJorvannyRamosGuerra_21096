from django.db import models

class Cliente(models.Model):
    dni = models.CharField(max_length=9, unique=True)
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
