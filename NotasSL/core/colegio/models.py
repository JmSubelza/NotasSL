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


class GestionRango(models.Model):
    name = models.CharField(max_length=100, verbose_name='Descripción', null=False)
    fecha_inicio = models.DateTimeField(verbose_name='Fecha Inicio', null=False)
    fecha_fin = models.DateTimeField(verbose_name='Fecha Final', null=False)
    gestion = models.ForeignKey(Gestion, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Gestión'
        verbose_name_plural = 'Gestiones'

