from django.db.models.deletion import DO_NOTHING
from django.urls import reverse
from django.db import models
from stdimage import StdImageField


class Group(models.Model):
    GroupName = models.CharField(
        max_length=60,
        verbose_name='Grupo',
        unique=True
    )

    class Meta:
        ordering = ('GroupName',)
        verbose_name = ("Grupo")
        verbose_name_plural = ("Grupos")

    def __str__(self):
        return self.GroupName


class Genre(models.Model):
    GenreName = models.CharField(
        max_length=60,
        verbose_name='Gênero',
        unique=True
    )

    class Meta:
        ordering = ('GenreName',)
        verbose_name = ("Gênero")
        verbose_name_plural = ("Gêneros")

    def __str__(self):
        return self.GenreName


class Brand(models.Model):
    BrandName = models.CharField(
        max_length=60,
        verbose_name='Marca',
        unique=True
    )

    class Meta:
        ordering = ('BrandName',)
        verbose_name = ("Marca")
        verbose_name_plural = ("Marcas")

    def __str__(self):
        return self.BrandName


class Product(models.Model):
    ProdutctsName = models.CharField(
        'Nome do Produto',
        max_length=100,
        unique=True
    )
    ProductPrice = models.DecimalField(
        null=True, blank=True,
        max_digits=7, decimal_places=2, verbose_name='Preço')
    # If Genre == Alimentício:
    DueDate = models.DateField(null=True, blank=True, verbose_name='Data de Vencimento')
    ProductImage = StdImageField(
        null=True, blank=True,
        verbose_name='Imagem', 
        upload_to='products/images', 
        variations={'thumb': {'width': 400, 'height': 400, 'crop': True}}
    )
    Description = models.TextField(
        null=True, blank=True, verbose_name='Descrição')
    CurrentStock = models.IntegerField(verbose_name='Estoque Atual')
    MinimumStock = models.PositiveIntegerField(
        'Estoque Mínimo',
        default=0
    )
    FkGenre = models.ForeignKey(
        Genre, null=True, blank=True, on_delete=DO_NOTHING, verbose_name='Gênero')
    FkGroup = models.ForeignKey(
        Group, null=True, blank=True, on_delete=DO_NOTHING, verbose_name='Grupo')
    FkBrand = models.ForeignKey(
        Brand, null=True, blank=True, on_delete=DO_NOTHING, verbose_name='Marca')

    class Meta:
        ordering = ('-ProdutctsName',)
        verbose_name = ("Produtos")
        verbose_name_plural = ("Produtos")

    def __str__(self) -> str:
        return self.ProdutctsName

    def get_absolute_url(self):
        return reverse("product:detail_product", kwargs={"pk": self.pk})
