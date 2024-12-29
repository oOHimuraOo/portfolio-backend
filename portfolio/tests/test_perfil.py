from django.test import TestCase
from portfolio.models import PerfilModel


class PerfilModelTestCase(TestCase):
    def setUp(self):
        self.perfil = PerfilModel.objects.create(
            image="http://example.com/image.png",
            nome_completo="John Doe",
            nick="johndoe",
            email="johndoe@example.com",
            github="http://github.com/johndoe",
            linkedin="http://linkedin.com/in/johndoe",
            profissao="Developer"
        )

    def test_perfil_creation(self):
        self.assertEqual(self.perfil.nome_completo, "John Doe")
        self.assertEqual(str(self.perfil), "John Doe")
