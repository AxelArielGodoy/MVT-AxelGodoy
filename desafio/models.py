import string
from django.db import models
from datetime import datetime

# Create your models here.

class Prueba(models.Model):
    nombre = models.CharField(max_length=30)
    numero = models.IntegerField()
    fecha = models.DateField()