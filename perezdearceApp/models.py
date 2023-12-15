from django.db import models

# Create your models here.
class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    email = models.EmailField()
    celular = models.IntegerField(max_length=9)
    fecha_nacimiento = models.DateField()
    password = models.CharField(max_length=20)

