from django.db import models

# Create your models here.
class Categoria(models):
    name = models.CharField(max_lenght=100) #atributo nombre
    #no se agrega el id porque ya se agrega automaticamente