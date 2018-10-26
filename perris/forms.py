from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona

        fields = [
            'nombre',
            'apellidos',
            'edad',
            'telefono',
            'email',
            'direccion',
        ]

        labels = {
            'nombre' : 'Nombre ',
            'apellidos' : 'Apellidos ',
            'edad' : 'Edad ',
            'telefono' : 'Telefono ',
            'email' : 'Email ',
            'direccion' : 'Dirección ',
        }

        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'apellidos' : forms.TextInput(attrs={'class':'form-control'}),
            'edad' : forms.TextInput(attrs={'class':'form-control'}),
            'telefono' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'direccion' : forms.TextInput(attrs={'class':'form-control'}),
        }