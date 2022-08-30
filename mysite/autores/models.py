from django.db import models

# Create your models here.
#Modelo para la entidad Autor. 
class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)