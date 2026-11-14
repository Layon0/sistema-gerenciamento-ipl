
from django.shortcuts import render, redirect, get_object_or_404

from .forms import (
    AnimalForm,
    RegistroVeterinarioForm,
    InteressadoForm,
    ProcessoAdocaoForm,
)
from .models import (
    Animal,
    RegistroVeterinario,
    Interessado,
    ProcessoAdocao,
)


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
    
    
def listar_interessados(request):
    interessados = Interessado.objects.all().order_by('nome')

    return render(
        request,
        'animais/listar_interessados.html',
        {'interessados': interessados}
    )


def cadastrar_interessado(request):
    if request.method == 'POST':
        form = InteressadoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar_interessados')
    else:
        form = InteressadoForm()

    return render(
        request,
        'animais/cadastrar_interessado.html',
        {'form': form}
    )


def listar_processos_adocao(request):
    processos = ProcessoAdocao.objects.select_related(
        'animal',
        'interessado'
    ).all()

    return render(
        request,
        'animais/listar_processos_adocao.html',
        {'processos': processos}
    )


def cadastrar_processo_adocao(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)

    if animal.status == Animal.Status.ADOTADO:
        return redirect('listar_animais')

    if request.method == 'POST':
        form = ProcessoAdocaoForm(request.POST)

        if form.is_valid():
            processo = form.save(commit=False)
            processo.animal = animal
            processo.save()

            animal.status = Animal.Status.EM_ADOCAO
            animal.save(update_fields=['status'])

            return redirect('listar_processos_adocao')
    else:
        form = ProcessoAdocaoForm()

    return render(
        request,
        'animais/cadastrar_processo_adocao.html',
        {'form': form, 'animal': animal}
    )
