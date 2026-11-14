from datetime import date

from django.test import TestCase
from .models import Animal


class AnimalModelTest(TestCase):

    def setUp(self):
        self.animal = Animal.objects.create(
            nome='Luna',
            especie='Cachorro',
            sexo='Fêmea',
            data_nascimento=date(2025, 1, 10),
            data_entrada=date(2026, 11, 14),
            descricao='Animal fictício para teste.',
        )

    def test_criar_animal(self):
        self.assertEqual(Animal.objects.count(), 1)

    def test_nome_animal(self):
        self.assertEqual(self.animal.nome, 'Luna')

    def test_status_padrao(self):
        self.assertEqual(
            self.animal.status,
            Animal.Status.DISPONIVEL
        )

    def test_representacao_textual(self):
        self.assertEqual(str(self.animal), 'Luna')
