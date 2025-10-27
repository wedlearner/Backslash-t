from django.db import models

class servicio(models.Model):
    titulo = models.CharField(max_length = 30, help_text ='Título del trabajo')
    trabajador = models.CharField(max_length = 30, help_text ='Nombre del trabajador')
    descripcion = models.TextField(help_text = 'Descripción del trabajo')


