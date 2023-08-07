from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
