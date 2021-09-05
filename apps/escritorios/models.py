from django.db import models

# Create your models here.
class Escritorio(models.Model):
    nome_escritorio = models.CharField(max_length=100, help_text='Nome do Escritório')

    class Meta:
        verbose_name_plural = 'Nome do Escritório'

    def __str__(self):
        return "{}".format(self.nome_escritorio)

