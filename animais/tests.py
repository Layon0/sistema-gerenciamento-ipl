from datetime import date

from django.test import TestCase
from .models import Animal, RegistroVeterinario


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


from django.urls import reverse


class AnimalViewsTest(TestCase):

    def setUp(self):
        self.animal = Animal.objects.create(
            nome='Rex',
            especie='Cachorro',
            sexo='Macho',
            data_entrada=date(2026, 11, 14),
            descricao='Animal fictício para teste.',
        )

    def test_listar_animais(self):
        response = self.client.get(
            reverse('listar_animais')
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Rex')

    def test_exibir_formulario_cadastro(self):
        response = self.client.get(
            reverse('cadastrar_animal')
        )

        self.assertEqual(response.status_code, 200)

    def test_cadastrar_animal(self):
        response = self.client.post(
            reverse('cadastrar_animal'),
            {
                'nome': 'Luna',
                'especie': 'Cachorro',
                'sexo': 'Fêmea',
                'data_entrada': '2026-11-14',
                'descricao': 'Animal fictício.',
                'status': 'Disponível',
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Animal.objects.filter(nome='Luna').exists()
        )

    def test_editar_animal(self):
        response = self.client.post(
            reverse(
                'editar_animal',
                args=[self.animal.id]
            ),
            {
                'nome': 'Rex Atualizado',
                'especie': 'Cachorro',
                'sexo': 'Macho',
                'data_entrada': '2026-11-14',
                'descricao': 'Descrição atualizada.',
                'status': 'Disponível',
            }
        )

        self.assertEqual(response.status_code, 302)

        self.animal.refresh_from_db()

        self.assertEqual(
            self.animal.nome,
            'Rex Atualizado'
        )

class RegistroVeterinarioTest(TestCase):

    def setUp(self):
        self.animal = Animal.objects.create(
            nome='Rex',
            especie='Cachorro',
            sexo='Macho',
            data_entrada=date(2026, 11, 14),
            descricao='Animal fictício para teste.',
        )

        self.registro = RegistroVeterinario.objects.create(
            animal=self.animal,
            data_registro=date(2026, 11, 14),
            tipo=RegistroVeterinario.Tipo.CONSULTA,
            descricao='Consulta veterinária de rotina.',
            profissional_responsavel='Dr. Carlos',
        )

    def test_criar_registro_veterinario(self):
        self.assertEqual(
            RegistroVeterinario.objects.count(),
            1
        )

    def test_registro_associado_ao_animal(self):
        self.assertEqual(
            self.registro.animal,
            self.animal
        )

    def test_tipo_registro(self):
        self.assertEqual(
            self.registro.tipo,
            RegistroVeterinario.Tipo.CONSULTA
        )

    def test_representacao_textual(self):
        self.assertEqual(
            str(self.registro),
            'Consulta - Rex'
        )

    def test_registros_ordenados_por_data(self):
        self.assertEqual(
            list(self.animal.registros_veterinarios.all()),
            [self.registro]
        )

class RegistroVeterinarioViewsTest(TestCase):

    def setUp(self):
        self.animal = Animal.objects.create(
            nome='Rex',
            especie='Cachorro',
            sexo='Macho',
            data_entrada=date(2026, 11, 14),
            descricao='Animal fictício para teste.',
        )

        self.registro = RegistroVeterinario.objects.create(
            animal=self.animal,
            data_registro=date(2026, 11, 14),
            tipo=RegistroVeterinario.Tipo.CONSULTA,
            descricao='Consulta veterinária de rotina.',
            profissional_responsavel='Dr. Carlos',
        )

    def test_listar_historico_veterinario(self):
        response = self.client.get(
            reverse(
                'listar_registros_veterinarios',
                args=[self.animal.id]
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Consulta veterinária de rotina.')

    def test_exibir_formulario_veterinario(self):
        response = self.client.get(
            reverse(
                'cadastrar_registro_veterinario',
                args=[self.animal.id]
            )
        )

        self.assertEqual(response.status_code, 200)

    def test_cadastrar_registro_veterinario(self):
        response = self.client.post(
            reverse(
                'cadastrar_registro_veterinario',
                args=[self.animal.id]
            ),
            {
                'data_registro': '2026-11-14',
                'tipo': 'Vacina',
                'descricao': 'Vacinação de rotina.',
                'profissional_responsavel': 'Dr. Carlos',
                'data_retorno': '',
            }
        )

        self.assertEqual(response.status_code, 302)

        self.assertTrue(
            RegistroVeterinario.objects.filter(
                animal=self.animal,
                tipo=RegistroVeterinario.Tipo.VACINA,
                descricao='Vacinação de rotina.',
            ).exists()
        )
