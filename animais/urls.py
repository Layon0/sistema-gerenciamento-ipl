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
]