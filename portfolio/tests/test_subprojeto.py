from django.test import TestCase
from portfolio.models import SubProjetoModel, ProjetoModel, TecnologiaModel


class SubProjetoModelTestCase(TestCase):
    def setUp(self):
        self.tecnologia = TecnologiaModel.objects.create(nome="Flask")
        self.projeto = ProjetoModel.objects.create(
            name="Projeto Flask",
            status=0,
            url="http://github.com/projeto-flask",
            description="Projeto de exemplo em Flask",
            tecnologia=self.tecnologia,
            icon="http://example.com/project-flask.png"
        )
        self.subprojeto = SubProjetoModel.objects.create(
            name="SubProjeto Flask",
            description="SubProjeto detalhado em Flask",
            status=1,
            tecnologia=self.tecnologia,
            projeto=self.projeto,
            icon="http://example.com/subproject.png"
        )

    def test_subprojeto_creation(self):
        self.assertEqual(self.subprojeto.name, "SubProjeto Flask")
        self.assertEqual(self.subprojeto.projeto.name, "Projeto Flask")
        self.assertEqual(str(self.subprojeto), "SubProjeto Flask")
