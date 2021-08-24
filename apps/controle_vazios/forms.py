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
                  'pol',
                'pod',
                  'navio',
                  'eta',
                  'armador',
                  'cmmdty',
                  'quantidade',
                  'type',
                  'status',
                  'cotacao',
                  'observacoes'
                  ]

    number_booking = forms.CharField(label="Nº BOOKING",  required=False)
    pol = forms.CharField(label="POL",  required=False)
    pod = forms.CharField(label="POD",  required=False)
    navio = forms.CharField(label="NAVIO",  required=False)
    eta = forms.DateField(widget=NumberInput(attrs={'type': 'date'}), label="ETA",  required=False)
    armador = forms.CharField(label="ARMADOR",  required=False)
    cmmdty = forms.CharField(label="COMMODITY",  required=False)
    quantidade = forms.DecimalField(label="QTD",  required=False)
    type = forms.CharField(label="TYPE",  required=False)
    status = forms.ChoiceField(widget=forms.Select(),
                               choices=([('Vazio', 'Vazio'), ('Vendido', 'Vendido')]), initial='',  required=False )
    cotacao = forms.CharField(label="COTAÇÃO",  required=False)
    observacoes = forms.CharField(widget=forms.Textarea(attrs={'rows':3}), label="OBSERVAÇÕES", required=False)


class VenderVaziosForm(forms.ModelForm):
    class Meta:
        model = ControleVazios

        fields = ['shipper',
                  'contrato_venda',
                  ]

    shipper = forms.CharField(label="Shipper")
    contrato_venda = forms.CharField(label="Contrato de Venda")
