from django.db import models

from user.models import User

class Shopping(models.Model):
    class ShoppingStatus(models.IntegerChoices):
        CARRINHO = (1,"Carrinho",)
        REALIZADO = (2,"Realizado",)
        PAGO = (3,"Pago",)
        ENTREGUE = (4,"Entregue",)

    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="shoppings")
    status = models.IntegerField(choices=ShoppingStatus.choices,  default=ShoppingStatus.CARRINHO)