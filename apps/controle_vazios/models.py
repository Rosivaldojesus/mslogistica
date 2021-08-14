from django.db import models

# Create your models here.

class ControleVazios(models.Model):
    number_booking = models.CharField(max_length=255)
    pol_pod = models.CharField(max_length=255)
    navio = models.CharField(max_length=255)
    eta = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True, verbose_name='ETA')
    armador = models.CharField(max_length=255)
    quantidade = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    type = models.CharField(max_length=255)
    STATUS_CHOICES = (
        ('Vazio', 'Vazio'),
        ('Vendido', 'Vendido'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    cotacao = models.CharField(max_length=255)
    observacoes = models.TextField()

    class Meta:
        verbose_name_plural = 'ControleVazios'

    def __str__(self):
        return "{}".format(self.number_booking)

