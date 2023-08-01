from django.db import models

# Create your models here.
# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"{self.nombre} ({self.comision})"
    
class Hogar(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Juguete(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Ropa(models.Model):
    nombre = models.CharField(max_length=50)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()  