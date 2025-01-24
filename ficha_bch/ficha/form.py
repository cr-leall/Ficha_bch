from django import forms
from . models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombres',
            'apellidos',
            'email',
            'username',
            'password',
            'roles',
        ]
