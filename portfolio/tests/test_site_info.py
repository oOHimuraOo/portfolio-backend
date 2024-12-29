from django.test import TestCase
from portfolio.models import SiteInfoModel, PerfilModel, FooterModel


class SiteInfoModelTestCase(TestCase):
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
        self.footer = FooterModel.objects.create(
            last_update="2024-12-01",
            views=1500,
            author="John Doe",
            made_in="Brazil",
            online=True
        )
        self.site_info = SiteInfoModel.objects.create(perfil=self.perfil, footer=self.footer)

    def test_site_info_creation(self):
        self.assertEqual(self.site_info.perfil.nome_completo, "John Doe")
        self.assertEqual(self.site_info.footer.author, "John Doe")
        self.assertEqual(str(self.site_info), "Site Info com perfil de John Doe")
