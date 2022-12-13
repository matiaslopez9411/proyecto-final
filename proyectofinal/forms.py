from django import forms
from proyectofinal.models import Jedi

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': 'Busque algo...'}))

class JediForm(forms.ModelForm):
    class Meta:
        model = Jedi
        fields = ['nombre','numero_jedi', 'titulo', 'color_sable']
