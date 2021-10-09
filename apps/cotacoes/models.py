from django.db import models

# Create your models here.
class Cotacoes(models.Model):
    quotation = models.CharField(max_length=255, blank=True, null=True)
    pol = models.CharField(max_length=255, blank=True, null=True)
    pod = models.CharField(max_length=255, blank=True, null=True)
    carrier = models.CharField(max_length=255, blank=True, null=True)
    cmmdty = models.CharField(max_length=255, blank=True, null=True)
    dv20 = models.CharField(max_length=255, blank=True, null=True)
    dv40 = models.CharField(max_length=255, blank=True, null=True)
    hc40 = models.CharField(max_length=255, blank=True, null=True)
    valid = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    detention = models.CharField(max_length=255, blank=True, null=True)
    demurrage = models.CharField(max_length=255, blank=True, null=True)
    data_cadastro = models.DateField(blank=True, null=True, verbose_name='Data do Cadastro')

    class Meta:
        verbose_name_plural = 'Cotações'

    def __str__(self):
        return "{}".format(self.pol)
