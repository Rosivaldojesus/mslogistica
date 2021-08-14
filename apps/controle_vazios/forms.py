from django import forms
from django.forms import NumberInput

from .models import ControleVazios



STATUS_CHOICES = [
    ('Vazio', 'Vazio'),
    ('Vendido', 'Vendido'),
]

class ControleVaziosForm(forms.ModelForm):
    class Meta:
        model = ControleVazios

        fields = ['number_booking',
                  'pol_pod',
                  'navio',
                  'eta',
                  'armador',
                  'quantidade',
                  'type',
                  'status',
                  'cotacao',
                  'observacoes'
                  ]

    number_booking = forms.CharField(label="Nº BOOKING")
    pol_pod = forms.CharField(label="POL X POD")
    navio = forms.CharField(label="NAVIO")
    eta = forms.DateField(widget=NumberInput(attrs={'type': 'date'}), label="ETA")
    armador = forms.CharField(label="ARMADOR")
    quantidade = forms.DecimalField(label="QTD")
    type = forms.CharField(label="TYPE")
    status = forms.ChoiceField(widget=forms.Select(),
                               choices=([('Vazio', 'Vazio'), ('Vendido', 'Vendido')]), initial='', required=True, )
    cotacao = forms.CharField(label="COTAÇÃO")
    observacoes = forms.CharField(widget=forms.Textarea(attrs={'rows':3}), label="OBSERVAÇÕES")