from django.db import models

# Create your models here.

class remeras(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    talle = models.TextField()
    cantidad_en_stock = models.IntegerField()

class buzos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    talle = models.TextField()
    cantidad_en_stock = models.IntegerField()

class pantalones(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    talle = models.TextField()
    cantidad_en_stock = models.IntegerField()