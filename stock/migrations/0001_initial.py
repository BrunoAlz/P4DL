# Generated by Django 3.2.8 on 2021-11-04 02:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreationDate', models.DateTimeField(auto_now_add=True, verbose_name='Criado em:')),
                ('ModificationDate', models.DateTimeField(auto_now=True, verbose_name='Modificado em:')),
                ('MovementStatus', models.CharField(choices=[('E', 'Entrada'), ('S', 'Saída'), ('D', 'Devolução'), ('I', 'Vencido')], max_length=1)),
                ('ResponsibleUser', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Estoque',
                'verbose_name_plural': 'Estoque',
                'ordering': ('-CreationDate',),
            },
        ),
        migrations.CreateModel(
            name='StockItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.PositiveIntegerField()),
                ('Balance', models.PositiveIntegerField()),
                ('FkProduct', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product')),
                ('FkStock', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='stock.stock')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
    ]