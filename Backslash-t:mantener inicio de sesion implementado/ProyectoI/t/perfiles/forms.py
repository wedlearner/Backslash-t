from django import forms
from .models import Perfil

class PerfilForm(forms.ModelForm):
    # Acá tiene que ir el código para implementar el campo de la fecha de nacimiento con DateField.
    
    
    class Meta:
        model = Perfil
        fields = ['nombre','telefono','mail','localidad','descripcion']