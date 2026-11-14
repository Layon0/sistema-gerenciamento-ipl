
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AnimalForm, RegistroVeterinarioForm
from .models import Animal, RegistroVeterinario


def listar_animais(request):
    animais = Animal.objects.all().order_by('nome')

    return render(
        request,
        'animais/listar_animais.html',
        {'animais': animais}
    )


def cadastrar_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar_animais')
    else:
        form = AnimalForm()

    return render(
        request,
        'animais/cadastrar_animal.html',
        {'form': form}
    )


def editar_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)

    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)

        if form.is_valid():
            form.save()
            return redirect('listar_animais')
    else:
        form = AnimalForm(instance=animal)

    return render(
        request,
        'animais/cadastrar_animal.html',
        {
            'form': form,
            'animal': animal,
        }
    )
def listar_registros_veterinarios(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)

    registros = animal.registros_veterinarios.all()

    return render(
        request,
        'animais/listar_registros_veterinarios.html',
        {
            'animal': animal,
            'registros': registros,
        }
    )


def cadastrar_registro_veterinario(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)

    if request.method == 'POST':
        form = RegistroVeterinarioForm(request.POST)

        if form.is_valid():
            registro = form.save(commit=False)
            registro.animal = animal
            registro.save()

            return redirect(
                'listar_registros_veterinarios',
                animal_id=animal.id
            )
    else:
        form = RegistroVeterinarioForm()

   
    return render(
        request,
        'animais/cadastrar_registro_veterinario.html',
        {
            'form': form,
            'animal': animal,
        }
    )