from django.db import models

from library.models import Author, Category, Publisher

class Book(models.Model):
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    amount = models.IntegerField(default=0, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, related_name='books')
    authors =  models.ManyToManyField(Author, related_name="books")

    def __str__(self):
        return f"{self.title} {self.amount}"