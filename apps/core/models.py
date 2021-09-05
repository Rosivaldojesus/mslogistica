from django.db import models

# Create your models here.
class Escritorio(models.Model):
    nome_escritorio = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        verbose_name_plural = 'Escritório'

    def __str__(self):
        return "{}".format(self.nome_escritorio)


