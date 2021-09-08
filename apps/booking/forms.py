from django import forms
from django.forms import NumberInput

from .models import Booking
from ..escritorios.models import Escritorio
from ..funcionarios.models import Funcionario



STATUS_CHOICES = [
    ('Vazio', 'Vazio'),
    ('Vendido', 'Vendido'),
]

class CadastrarBookingForm(forms.ModelForm):
    class Meta:
        model = Booking

        fields = ['number_booking',
                  'escritorio',
                  'pol',
                  'pod',
                  'navio',
                  'eta',
                  'armador',
                  'cmmdty',
                  'quantidade',
                  'type',
                  'cotacao',
                  'shipper',
                  'contrato_venda',
                  'cadastrado_por',
                  'vendido_por',
                  'observacoes'
        ]

    number_booking = forms.CharField(label="Nº Booking:",  required=False)
    escritorio = forms.ModelChoiceField(queryset=Escritorio.objects.all().order_by('nome_escritorio'), label="Escritório:")
    pol = forms.CharField(label="Pol:",  required=False)
    pod = forms.CharField(label="Pod:",  required=False)
    navio = forms.CharField(label="Navio:",  required=False)
    eta = forms.DateField(widget=NumberInput(attrs={'type': 'date'}), label="Eta:",  required=False)
    armador = forms.CharField(label="Armador:",  required=False)
    cmmdty = forms.CharField(label="Commodity:",  required=False)
    quantidade = forms.DecimalField(label="Quantidade:",  required=False)
    type = forms.CharField(label="Type:",  required=False)
    shipper = forms.CharField(label="Shipper:",  required=False)
    cotacao = forms.CharField(label="Cotação:",  required=False)
    contrato_venda = forms.CharField(label="Contrato de Venda:",  required=False)
    cadastrado_por = forms.ModelChoiceField(queryset=Funcionario.objects.all().order_by(), label="Quem Cadastrou?:")
    vendido_por = forms.ModelChoiceField(queryset=Funcionario.objects.all().order_by(), label="Quem vendeu?:")
    observacoes = forms.CharField(widget=forms.Textarea(attrs={'rows':3}), label="Observações:", required=False)




class EditarBookingForm(forms.ModelForm):
    class Meta:
        model = Booking

        fields = ['number_booking',
                  'escritorio',
                  'pol',
                  'pod',
                  'navio',
                  'eta',
                  'armador',
                  'cmmdty',
                  'quantidade',
                  'type',
                  'cotacao',
                  'shipper',
                  'contrato_venda',
                  'cadastrado_por',
                  'vendido_por',
                  'observacoes'
        ]

    number_booking = forms.CharField(label="Nº Booking:",  required=False)
    escritorio = forms.ModelChoiceField(queryset=Escritorio.objects.all().order_by('nome_escritorio'), label="Escritório:")
    pol = forms.CharField(label="Pol:",  required=False)
    pod = forms.CharField(label="Pod:",  required=False)
    navio = forms.CharField(label="Navio:",  required=False)
    eta = forms.DateField(widget=NumberInput(attrs={'type': 'date'}), label="Eta:",  required=False)
    armador = forms.CharField(label="Armador:",  required=False)
    cmmdty = forms.CharField(label="Commodity:",  required=False)
    quantidade = forms.DecimalField(label="Quantidade:",  required=False)
    type = forms.CharField(label="Type:",  required=False)
    shipper = forms.CharField(label="Shipper:",  required=False)
    cotacao = forms.CharField(label="Cotação:",  required=False)
    contrato_venda = forms.CharField(label="Contrato de Venda:",  required=False)

    cadastrado_por = forms.ModelChoiceField(queryset=Funcionario.objects.all().order_by(), label="Quem Cadastrou?:")
    vendido_por = forms.ModelChoiceField(queryset=Funcionario.objects.all().order_by(), label="Quem vendeu?:")

    observacoes = forms.CharField(widget=forms.Textarea(attrs={'rows':3}), label="Observações:", required=False)




class VenderBookingForm(forms.ModelForm):
    class Meta:
        model = Booking

        fields = ['shipper',
                  'contrato_venda',
                  ]
    shipper = forms.CharField(label="Shipper")
    contrato_venda = forms.CharField(label="Contrato de Venda")
