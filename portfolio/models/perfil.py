from django.db import models


class PerfilModel(models.Model):
    image = models.URLField(max_length=200)
    nome_completo = models.CharField(max_length=255)
    nick = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, null=True)
    github = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)
    profissao = models.CharField(max_length=100)

    class Meta:
        verbose_name = "perfil"
        verbose_name_plural = "perfis"
        constraints = [
            models.UniqueConstraint(
                fields=["id"],
                name="unique_perfil_constraint",
            )
        ]

    def __str__(self):
        return self.nome_completo
