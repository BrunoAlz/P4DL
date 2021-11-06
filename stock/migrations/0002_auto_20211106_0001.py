# Generated by Django 3.2.8 on 2021-11-06 03:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20211106_0001'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stockitems',
            options={'ordering': ('pk',), 'verbose_name': 'Itens do Estoque', 'verbose_name_plural': 'Itens do Estoque'},
        ),
        migrations.AlterField(
            model_name='stock',
            name='MovementStatus',
            field=models.CharField(choices=[('E', 'Entrada'), ('S', 'Saída'), ('D', 'Devolução'), ('I', 'Vencido')], max_length=1, verbose_name='Motivo'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='ResponsibleUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Responsável'),
        ),
        migrations.AlterField(
            model_name='stockitems',
            name='Balance',
            field=models.PositiveIntegerField(verbose_name='Saldo'),
        ),
        migrations.AlterField(
            model_name='stockitems',
            name='FkProduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product', verbose_name='FkProduto'),
        ),
        migrations.AlterField(
            model_name='stockitems',
            name='Quantity',
            field=models.PositiveIntegerField(verbose_name='Quantidade'),
        ),
    ]