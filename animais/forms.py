
from django import forms
from .models import (
    Animal,
    RegistroVeterinario,
    Interessado,
    ProcessoAdocao,
)


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

class InteressadoForm(forms.ModelForm):
    class Meta:
        model = Interessado
        fields = [
            'nome',
            'email',
            'telefone',
        ]

        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome completo',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email@exemplo.com',
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(00) 00000-0000',
            }),
        }


class ProcessoAdocaoForm(forms.ModelForm):
    class Meta:
        model = ProcessoAdocao
        fields = [
            'interessado',
            'status',
            'observacoes',
        ]

        widgets = {
            'interessado': forms.Select(attrs={
                'class': 'form-select',
            }),
            'status': forms.Select(attrs={
                'class': 'form-select',
            }),
            'observacoes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Observações sobre o processo de adoção',
            }),
        }
