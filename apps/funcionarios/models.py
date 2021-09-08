from django.db import models
from django.contrib.auth.models import User
from ..escritorios.models import Escritorio
from ..departamentos.models import Departamento

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    escritorio = models.ForeignKey(Escritorio, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return "{}".format(self.nome)





