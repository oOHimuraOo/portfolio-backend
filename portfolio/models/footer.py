from django.db import models


class FooterModel(models.Model):
    last_update = models.CharField(max_length=100)
    views = models.PositiveIntegerField(default=0)
    author = models.CharField(max_length=255)
    made_in = models.CharField(max_length=255)
    online = models.BooleanField(default=True)

    class Meta:
        verbose_name = "footer"
        verbose_name_plural = "footers"
        constraints = [
            models.UniqueConstraint(
                fields=["id"],
                name="unique_footer_constraint",
            )
        ]

    def __str__(self):
        return f"Footer atualizado em {self.last_update}"
