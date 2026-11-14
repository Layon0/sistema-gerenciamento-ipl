
from django import forms
from .models import Animal


class AnimalForm(forms.ModelForm):

    class Meta:
        model = Animal
        fields = [
            'nome',
            'especie',
            'sexo',
            'data_nascimento',
            'data_entrada',
            'descricao',
            'status',
        ]

        widgets = {
            'data_nascimento': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'data_entrada': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'descricao': forms.Textarea(
                attrs={'rows': 3}
            ),
        }
