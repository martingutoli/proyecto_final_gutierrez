from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Inmuebles (models.Model):
    tipo_de_operacion = models.CharField(max_length=100)
    precio = models.IntegerField()
    cantidad_ambientes = models.IntegerField()
    cantidad_dormitorios = models.IntegerField()
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.tipo_de_operacion} - {self.precio} - {self.cantidad_ambientes} - {self.cantidad_dormitorios} - {self.descripcion}"



#class Avatar(models.Model):

 #   usuario = models.ForeignKey(User, on_delete=models.CASCADE)
  #  imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
