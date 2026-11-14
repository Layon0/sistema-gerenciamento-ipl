
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
]
