from django.db import models


class TecnologiaModel(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    logo = models.URLField(max_length=200)

    class Meta:
        verbose_name = "tecnologia"
        verbose_name_plural = "tecnologias"

    def __str__(self):
        return self.nome
