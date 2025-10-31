from django.db import models

class servicio(models.Model):
    titulo = models.CharField(max_length = 30, help_text ='Título del trabajo')
    precio = models.IntegerField(help_text='Precio del servicio en pesos')
    trabajador = models.ForeignKey('perfiles.Perfil', on_delete=models.CASCADE)
    descripcion = models.TextField(help_text = 'Descripción del trabajo')

    def __str__(self):
        return self.titulo

