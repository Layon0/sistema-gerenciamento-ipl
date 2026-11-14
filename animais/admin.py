
from django.contrib import admin
from .models import (
    Animal,
    RegistroVeterinario,
    Interessado,
    ProcessoAdocao,
)


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'especie',
        'sexo',
        'data_entrada',
        'status',
    )

    list_filter = ('especie', 'status')
    search_fields = ('nome',)
    ordering = ('nome',)


@admin.register(RegistroVeterinario)
class RegistroVeterinarioAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'animal',
        'data_registro',
        'tipo',
        'profissional_responsavel',
        'data_retorno',
    )

    list_filter = ('tipo', 'data_registro')
    search_fields = (
        'animal__nome',
        'descricao',
        'profissional_responsavel',
    )

    ordering = ('-data_registro',)

@admin.register(Interessado)
class InteressadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'email',
        'telefone',
        'data_cadastro',
    )

    search_fields = ('nome', 'email', 'telefone')
    ordering = ('nome',)


@admin.register(ProcessoAdocao)
class ProcessoAdocaoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'animal',
        'interessado',
        'status',
        'data_solicitacao',
        'data_conclusao',
    )

    list_filter = ('status', 'data_solicitacao')
    search_fields = (
        'animal__nome',
        'interessado__nome',
        'interessado__email',
    )

    ordering = ('-data_solicitacao',)
