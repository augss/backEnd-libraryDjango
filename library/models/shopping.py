from django.db import models

from library.models import Book
from user.models import User

class Shopping(models.Model):
    class ShoppingStatus(models.IntegerChoices):
        CARRINHO = (1,"Carrinho",)
        REALIZADO = (2,"Realizado",)
        PAGO = (3,"Pago",)
        ENTREGUE = (4,"Entregue",)

    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="shoppings")
    status = models.IntegerField(choices=ShoppingStatus.choices,  default=ShoppingStatus.CARRINHO)

class ShoppingItem(models.Model):
    shopping = models.ForeignKey(Shopping, on_delete=models.CASCADE, related_name="items")
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name="+")
    amount = models.IntegerField(default=1)