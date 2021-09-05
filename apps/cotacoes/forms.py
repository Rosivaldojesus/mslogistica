from django import forms
from django.forms import NumberInput

from .models import Cotacoes

class CotacoesForm(forms.ModelForm):
    class Meta:
        model = Cotacoes
        fields = ['pol', 'pod', 'carrier', 'quotation', 'cmmdty', 'dv20', 'dv40', 'hc40', 'detention', 'demurrage', 'valid' ]

    pol = forms.CharField(label="Pol:", required=False)
    pod = forms.CharField(label="Pod:", required=False)
    carrier = forms.CharField(label="Carrier:", required=False)
    quotation = forms.CharField(label="Quotation:", required=False)
    cmmdty = forms.CharField(label="Commodity:", required=False)
    dv20 = forms.CharField(label="DV´20:", required=False)
    dv40 = forms.CharField(label="DV´40:", required=False)
    hc40 = forms.CharField(label="HC´40:", required=False)
    detention = forms.CharField(label="Detention:", required=False)
    demurrage = forms.CharField(label="Demurrage:", required=False)

    valid = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

