from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=150)
    mensaje = models.CharField(max_length=600)

    def __str__(self):
        return f"{self.nombre} - {self.mensaje}"