from django.db import models

# Create your models here.
class Usuarios(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    email = models.EmailField()
    celular = models.IntegerField()
    fecha_nacimiento = models.DateField()
    password = models.CharField(max_length=20)

