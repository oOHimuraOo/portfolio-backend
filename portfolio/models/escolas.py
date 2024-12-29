from django.db import models


class EscolasModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = models.URLField(max_length=200)

    class Meta:
        verbose_name = "escola"
        verbose_name_plural = "escolas"

    def __str__(self):
        return self.name
