from django.test import TestCase
from portfolio.models import ProjetoModel, TecnologiaModel


class ProjetoModelTestCase(TestCase):
    def setUp(self):
        self.tecnologia = TecnologiaModel.objects.create(nome="Django")
        self.projeto = ProjetoModel.objects.create(
            name="Projeto Django",
            status=0,
            url="http://github.com/projeto-django",
            description="Projeto de exemplo em Django",
            tecnologia=self.tecnologia,
            icon="http://example.com/project.png"
        )

    def test_projeto_creation(self):
        self.assertEqual(self.projeto.name, "Projeto Django")
        self.assertEqual(self.projeto.tecnologia.nome, "Django")
        self.assertEqual(str(self.projeto), "Projeto Django")
