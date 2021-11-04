from django.db import models


class Product(models.Model):
    ProdutctsName = models.CharField(
        'Nome do Produto',
        max_length=100,
        unique=True
    )
    Stock = models.IntegerField('Estoque Atual'),
    MinimumStock = models.PositiveIntegerField(
        'Estoque Mínimo',
        default=0
    )

    class Meta:
        verbose_name = ("Produtos")
        verbose_name_plural = ("Produtos")

    def __str__(self):
        return self.ProdutctsName
