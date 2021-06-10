from django.db import models


# Create your models here.

class Gestion(models.Model):
    name = models.CharField(max_length=100, verbose_name='Descripción', null=False)
    year = models.PositiveIntegerField(unique=True, verbose_name='Año')

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Gestión'
        verbose_name_plural = 'Gestiones'
        ordering = ['year']
