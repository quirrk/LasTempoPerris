from django.db import models

# Create your models here.
class Persona(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    direccion = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre

class Perro(models.Model):
    estado_opc = (
        ('AD', 'Adoptado'),
        ('RE', 'Rescatado'),
        ('DI', 'Disponible'),
    )
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    descripcion = models.TextField()
    estado = models.CharField(max_length=2, choices=estado_opc)
    foto = models.ImageField(upload_to='media/rescatados/')
    def __str__(self):
        return self.nombre