
from django.db import models


class Animal(models.Model):

    class Especie(models.TextChoices):
        CACHORRO = 'Cachorro', 'Cachorro'
        GATO = 'Gato', 'Gato'

    class Status(models.TextChoices):
        DISPONIVEL = 'Disponível', 'Disponível'
        EM_TRATAMENTO = 'Em tratamento', 'Em tratamento'
        EM_ADOCAO = 'Em processo de adoção', 'Em processo de adoção'
        ADOTADO = 'Adotado', 'Adotado'

    nome = models.CharField(max_length=100)
    especie = models.CharField(
        max_length=20,
        choices=Especie.choices
    )
    sexo = models.CharField(max_length=20, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    data_entrada = models.DateField()
    descricao = models.TextField(blank=True)
    status = models.CharField(
        max_length=30,
        choices=Status.choices,
        default=Status.DISPONIVEL
    )

    def __str__(self):
        return self.nome
