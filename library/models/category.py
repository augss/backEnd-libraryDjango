from django.db import models

class Category(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'