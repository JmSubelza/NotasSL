from django.db import models


# Create your models here.
class Materia(models.Model):
    name = models.CharField(unique=True, max_length=100, verbose_name='Descripción')
    is_active = models.BooleanField(verbose_name='Activo', default=True)

    def __str__(self):
        return '{}'.format(self.name)
