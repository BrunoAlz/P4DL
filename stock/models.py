from django.contrib.auth.models import User
from django.db import models
from core.models import TimeStampedModel
from product.models import Product
from utils.constants import MOVIMENT


class Stock(TimeStampedModel):
    """
    Aqui teremos o Usuário que efetivou a alteração no estoque,
    seja incluindo ou excluindo.. esse usuário está Herdando a classe User
    do Admin do Django
    """
    ResponsibleUser = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    MovementStatus = models.CharField(max_length=1, choices=MOVIMENT)

    class Meta:
        ordering = ('-CreationDate',)
        verbose_name = ("Estoque")
        verbose_name_plural = ("Estoque")

    def __str__(self) -> str:
        return str(self.pk)


class StockItems(models.Model):
    """
    Aqui faremos uma tabela auxiliar para poder gravar as alterações em cada
    item de nosso estoque, bem como as quantidades de entrada e saida e o 
    saldo final.
    """
    FkStock = models.ForeignKey(Stock, on_delete=models.DO_NOTHING)
    FkProduct = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    Quantity = models.PositiveIntegerField()
    Balance = models.PositiveIntegerField()

    class Meta:
        ordering = ('pk',)

    def __str__(self) -> str:
        return f'{self.pk} - {self.FkStock.pk} - {self.FkProduct}'
