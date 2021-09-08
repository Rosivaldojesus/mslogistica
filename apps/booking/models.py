from django.db import models
from django.contrib.auth.models import User
from ..escritorios.models import Escritorio
from django.utils import timezone


# Create your models here.

class Booking(models.Model):
    number_booking = models.CharField(max_length=255, blank=True, null=True, verbose_name='Nº. Booking')
    pol = models.CharField(max_length=255, blank=True, null=True)
    pod = models.CharField(max_length=255, blank=True, null=True)
    navio = models.CharField(max_length=255, blank=True, null=True)
    commodity = models.CharField(max_length=255, blank=True, null=True)
    eta = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True, verbose_name='ETA')
    armador = models.CharField(max_length=255, blank=True, null=True)
    quantidade = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    STATUS_CHOICES = (
        ('Vazio', 'Vazio'),
        ('Vendido', 'Vendido'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    cotacao = models.CharField(max_length=255, blank=True, null=True)
    shipper = models.CharField(max_length=255, blank=True, null=True)
    contrato_venda = models.CharField(max_length=255, blank=True, null=True)
    cadastrado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='Cadastrado_Por_Por', blank=True, null=True)
    data_cadastro = models.DateField(blank=True, null=True, verbose_name='Data do Cadastro')
    vendido_por = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='Vendido_Por_Por', blank=True, null=True)
    data_venda = models.DateField(blank=True, null=True, verbose_name='Data da Venda')
    vendido_por_filial = models.ForeignKey(Escritorio, on_delete=models.DO_NOTHING, related_name='Vendido_Por_Filial_Por', blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Booking'

    def __str__(self):
        return "{}".format(self.number_booking)

