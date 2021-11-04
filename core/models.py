from django.db import models


class TimeStampedModel(models.Model):
    """
    Model para controle de Criação e alteração de dados no Banco.
    """
    CreationDate  = models.DateTimeField(
        'Criado em:',
        auto_now_add=True,
        auto_now=False
    )
    ModificationDate  = models.DateTimeField(
        'Modificado em:',
        auto_now_add=False,
        auto_now=True
    )

    class Meta:
        """
        o Abstract indica que essa model será herdada em outras Models,
        que receberão os Atributos CreationDate e ModificationDate
        Indicando a data de Criação dos dados no Banco quando eles foram
        criados e a data de modificação assim que sofrerem alterações
        """
        abstract = True

