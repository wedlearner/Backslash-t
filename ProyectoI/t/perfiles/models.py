from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length = 30, help_text = 'Nombre completo')
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length = 12, help_text = 'Teléfono')
    mail = models.EmailField(help_text = 'Correo electrónico' )
    localidad = models.CharField(max_length = 30, help_text = 'Localidad')
    descripcion = models.TextField(help_text = 'Incluya información sobre usted para que otros le conozcan')


# Create your models here.
