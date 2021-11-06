from django.urls import reverse
from django.db import models


class Product(models.Model):
    ProdutctsName = models.CharField(
        'Nome do Produto',
        max_length=100,
        unique=True
    )
    CurrentStock = models.IntegerField(verbose_name='Estoque Atual')
    MinimumStock = models.PositiveIntegerField(
        'Estoque Mínimo',
        default=0
    )

    class Meta:
        verbose_name = ("Produtos")
        verbose_name_plural = ("Produtos")

    def __str__(self) -> str:
        return self.ProdutctsName

    def get_absolute_url(self):
        return reverse("product:detail_product", kwargs={"pk": self.pk})
