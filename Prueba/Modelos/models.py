from django.db import models

# Create your models here.
class Estudiantes (models.Model):
    cedula = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=30, blank=False)
    apellido = models.TextField()
    edad = models.IntegerField()
    direccion = models.TextField()
    telefono = models.CharField(max_length=10)

    def __str__ (self):
        return self.nombre

class Docente (models.Model):
    cedula = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=30, blank=False)
    apellido = models.TextField()

    def __str__ (self):
        return self.nombre
    
class Calificacion (models.Model):
    estudiante = models.ForeignKey(Estudiantes, on_delete=models.RESTRICT)
    docente = models.ForeignKey(Docente, on_delete=models.RESTRICT)
    nota = models.FloatField ()
    