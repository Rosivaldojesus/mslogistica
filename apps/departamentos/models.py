from django.db import models
from ..escritorios.models import Escritorio
# Create your models here.
class Departamento(models.Model):
    nome = models.CharField(max_length=70)
    empresa = models.ForeignKey(Escritorio, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return "{}".format(self.nome)
