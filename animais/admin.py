
from django.contrib import admin
from .models import Animal, RegistroVeterinario


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
