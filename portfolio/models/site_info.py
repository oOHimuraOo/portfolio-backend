from django.db import models


class SiteInfoModel(models.Model):
    perfil = models.OneToOneField(
        "portfolio.PerfilModel", on_delete=models.CASCADE, related_name="site_info"
    )
    footer = models.OneToOneField(
        "portfolio.FooterModel", on_delete=models.CASCADE, related_name="site_info"
    )
    cursos = models.OneToOneField(
        "portfolio.CursoModel", on_delete=models.CASCADE, related_name="site_info", blank=True, null=True
    )
    projetos = models.OneToOneField(
        "portfolio.ProjetoModel", on_delete=models.CASCADE, related_name="site_info", blank=True, null=True
    )

    class Meta:
        verbose_name = "informação do site"
        verbose_name_plural = "informações do site"

    def __str__(self):
        return f"Site Info com perfil de {self.perfil.nome_completo}"
