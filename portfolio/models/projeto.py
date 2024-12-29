from django.db import models


class ProjetoModel(models.Model):
    name = models.CharField(max_length=100)
    status = models.IntegerField(
        choices=[
            (0, "completed"),
            (1, "incomplete"),
            (2, "dropped"),
        ],
        default=1,
    )
    url = models.URLField(max_length=200, blank=True, null=True)
    description = models.TextField()
    conclusion = models.TextField(blank=True, null=True)
    code_ex = models.TextField(blank=True, null=True)
    tecnologia = models.ForeignKey("portfolio.TecnologiaModel", on_delete=models.CASCADE)
    icon = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
