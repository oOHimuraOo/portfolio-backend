from django.test import TestCase
from portfolio.models import CursoModel, EscolasModel, TecnologiaModel


class CursoModelTestCase(TestCase):
    def setUp(self):
        self.tecnologia = TecnologiaModel.objects.create(nome="Python")
        self.escola = EscolasModel.objects.create(name="Udemy", logo="http://example.com/udemy.png")
        self.curso = CursoModel.objects.create(
            nome="Curso Python",
            tecnologia=self.tecnologia,
            escola=self.escola,
            icon="http://example.com/course.png",
            codigo_cert="CERT123",
            status=0,
            descricao="Curso de Python completo",
            url="http://example.com/python-course"
        )

    def test_curso_creation(self):
        self.assertEqual(self.curso.nome, "Curso Python")
        self.assertEqual(self.curso.tecnologia.nome, "Python")
        self.assertEqual(str(self.curso), "Curso Python")
