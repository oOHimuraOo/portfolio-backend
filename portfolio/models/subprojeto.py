from django.db import models

class SubProjetoModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    conclusion = models.TextField(blank=True, null=True)
    code_ex = models.TextField(blank=True, null=True)
    status = models.IntegerField(
        choices=[
            (0, "completed"),
            (1, "incomplete"),
            (2, "dropped"),
        ],
        default=1,
    )
    tecnologia = models.ForeignKey("portfolio.TecnologiaModel", on_delete=models.CASCADE)
    icon = models.URLField(max_length=200, blank=True, null=True)

    # Relacionamento com ProjetoModel
    projeto = models.ForeignKey(
        "portfolio.ProjetoModel",
        on_delete=models.CASCADE,
        related_name="subprojetos"
    )

    def __str__(self):
        return self.name
