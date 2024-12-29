from django.db import models


class CursoModel(models.Model):
    nome = models.CharField(max_length=100)
    tecnologia = models.ForeignKey("portfolio.TecnologiaModel", on_delete=models.CASCADE)
    escola = models.ForeignKey("portfolio.EscolasModel", on_delete=models.CASCADE)
    icon = models.URLField(max_length=200, blank=True, null=True)
    codigo_cert = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(
        choices=[
            (0, "completed"),
            (1, "incomplete"),
            (2, "dropped"),
        ],
        default=1,
    )
    descricao = models.TextField()
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.nome