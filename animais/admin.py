from django.contrib import admin
from .models import Animal


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