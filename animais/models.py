
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

class RegistroVeterinario(models.Model):

    class Tipo(models.TextChoices):
        CONSULTA = 'Consulta', 'Consulta'
        VACINA = 'Vacina', 'Vacina'
        EXAME = 'Exame', 'Exame'
        TRATAMENTO = 'Tratamento', 'Tratamento'

    animal = models.ForeignKey(
        Animal,
        on_delete=models.CASCADE,
        related_name='registros_veterinarios'
    )

    data_registro = models.DateField()

    tipo = models.CharField(
        max_length=20,
        choices=Tipo.choices
    )

    descricao = models.TextField()

    profissional_responsavel = models.CharField(
        max_length=100,
        blank=True
    )

    data_retorno = models.DateField(
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['-data_registro']

    def __str__(self):
        return f'{self.tipo} - {self.animal.nome}'

class Interessado(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    data_cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome


class ProcessoAdocao(models.Model):

    class Status(models.TextChoices):
        INTERESSE = 'Interesse', 'Interesse'
        ANALISE = 'Em análise', 'Em análise'
        ENTREVISTA = 'Entrevista', 'Entrevista'
        VISITA = 'Visita', 'Visita'
        APROVADO = 'Aprovado', 'Aprovado'
        CONCLUIDO = 'Concluído', 'Concluído'
        ENCERRADO = 'Encerrado', 'Encerrado'

    animal = models.ForeignKey(
        Animal,
        on_delete=models.PROTECT,
        related_name='processos_adocao'
    )

    interessado = models.ForeignKey(
        Interessado,
        on_delete=models.PROTECT,
        related_name='processos_adocao'
    )

    data_solicitacao = models.DateField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.INTERESSE
    )

    observacoes = models.TextField(blank=True)

    data_conclusao = models.DateField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.interessado.nome} - {self.animal.nome}'
