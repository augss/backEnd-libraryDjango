from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Publisher'
        verbose_name_plural = 'Publishers'