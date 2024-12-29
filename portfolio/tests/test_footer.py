from django.test import TestCase
from portfolio.models import FooterModel


class FooterModelTestCase(TestCase):
    def setUp(self):
        self.footer = FooterModel.objects.create(
            last_update="2024-12-01",
            views=1500,
            author="John Doe",
            made_in="Brazil",
            online=True
        )

    def test_footer_creation(self):
        self.assertEqual(self.footer.author, "John Doe")
        self.assertEqual(self.footer.views, 1500)
        self.assertEqual(str(self.footer), "Footer atualizado em 2024-12-01")
