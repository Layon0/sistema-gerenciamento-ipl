from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_animais, name='listar_animais'),
    path('cadastrar/', views.cadastrar_animal, name='cadastrar_animal'),
    path(
        'editar/<int:animal_id>/',
        views.editar_animal,
        name='editar_animal'
    ),
    path(
        '<int:animal_id>/historico/',
        views.listar_registros_veterinarios,
        name='listar_registros_veterinarios'
    ),
    path(
        '<int:animal_id>/historico/cadastrar/',
        views.cadastrar_registro_veterinario,
        name='cadastrar_registro_veterinario'
    ),
    path(
    'interessados/',
    views.listar_interessados,
    name='listar_interessados'
    ),
    path(
        'interessados/cadastrar/',
        views.cadastrar_interessado,
        name='cadastrar_interessado'
    ),
    path(
        'processos-adocao/',
        views.listar_processos_adocao,
        name='listar_processos_adocao'
    ),
    path(
        '<int:animal_id>/iniciar-adocao/',
        views.cadastrar_processo_adocao,
        name='cadastrar_processo_adocao'
    ),
]
