from django.db import models

class Entrenador(models.Model):
    nombre = models.CharField(max_length=200)
    especialidad = models.CharField(max_length=200)
    biografia = models.TextField()  #El CV
    
class Socio(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    observaciones_medicas = models.TextField() #Observaciones médicas
    fecha_alta = models.DateTimeField()
    
class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    sala = models.CharField(max_length=50)
    fecha_inicio = models.DateTimeField() #Dia y hora de la clase
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE)

# Create your models here.
