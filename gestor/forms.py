from django import forms
from .models import Categoria, Transaccion

class CategoriaForm(forms.ModelForm):
    class Meta:
        model: Categoria
        fields = ['nombre', 'tipo']
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Salario, Comida'}),
            "descripcion": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción opcional'}),
        }

class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = ['categoria', 'monto', 'fecha', 'descripcion']
        widgets = {
            "categoria": forms.Select(attrs={'class': 'form-control'}),
            "monto": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 1000'}),
            "fecha": forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            "descripcion": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción opcional'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)