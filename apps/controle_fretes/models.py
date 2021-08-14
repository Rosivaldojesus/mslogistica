from django.db import models

# Create your models here.
class ControleFretes(models.Model):
    pol = models.CharField(max_length=255)
    pod = models.CharField(max_length=255)
    carrier = models.CharField(max_length=255)
    quotation = models.CharField(max_length=255)
    cmmdty = models.CharField(max_length=255)
    dv20 = models.CharField(max_length=255)
    dv40 = models.CharField(max_length=255)
    hc40 = models.CharField(max_length=255)
    valid = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    detention = models.CharField(max_length=255)
    demurrage = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'ControleFretes'

    def __str__(self):
        return "{}".format(self.pol)
