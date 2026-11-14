
from django import forms
from .models import Animal, RegistroVeterinario


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
class RegistroVeterinarioForm(forms.ModelForm):

    class Meta:
        model = RegistroVeterinario
        fields = [
            'data_registro',
            'tipo',
            'descricao',
            'profissional_responsavel',
            'data_retorno',
        ]

        widgets = {
            'data_registro': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'data_retorno': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'descricao': forms.Textarea(
                attrs={'rows': 4}
            ),
        }