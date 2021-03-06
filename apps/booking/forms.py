from datetime import date

from django import forms
from django.forms import NumberInput

from .models import Booking
from ..escritorios.models import Escritorio
from ..cotacoes.models import Cotacoes
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
                  'commodity',
                  'quantidade',
                  'type',
                  'cotacao',
                  'data_ddl_draft',
                  'hora_ddl_draft',
                  'cotacoes',
                  'observacoes'
        ]

    number_booking = forms.CharField(label="Nº Booking:",  required=True)
    escritorio = forms.ModelChoiceField(queryset=Escritorio.objects.all().order_by('nome_escritorio'), label="Escritório:",required=True)
    pol = forms.CharField(label="Pol:",  required=False)
    pod = forms.CharField(label="Pod:",  required=False)
    navio = forms.CharField(label="Navio:",  required=False)
    eta = forms.DateField(widget=NumberInput(attrs={'type': 'date'}), label="Eta:",  required=False)
    armador = forms.CharField(label="Armador:",  required=False)
    commodity = forms.CharField(label="Commodity:",  required=False)
    quantidade = forms.DecimalField(label="Quantidade:",  required=False)
    type = forms.CharField(label="Type:",  required=False)
    #shipper = forms.CharField(label="Shipper:",  required=False)
    cotacao = forms.CharField(label="Cotação:",  required=False)
    data_ddl_draft = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}),label="Data DDL:",  required=False)
    hora_ddl_draft = forms.TimeField(widget=forms.DateInput(attrs={"type": "time"}), label="Hora DDL:",  required=False)

    cotacoes = forms.ModelChoiceField(queryset=Cotacoes.objects.values_list('quotation', flat = True), label="Cotações:",required=True)

    #contrato_venda = forms.CharField(label="Contrato de Venda:",  required=False)

    #cadastrado_por = forms.ModelChoiceField(queryset=Funcionario.objects.all().order_by(), label="Quem Cadastrou?:")
    #vendido_por = forms.ModelChoiceField(queryset=Funcionario.objects.all().order_by(), label="Quem vendeu?:")

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
                  'commodity',
                  'quantidade',
                  'type',
                  'cotacao',
                  'data_ddl_draft',
                  'hora_ddl_draft',
                  'shipper',
                  'contrato_venda',
                  'cadastrado_por',
                  'vendido_por',

                  'observacoes',


        ]

    number_booking = forms.CharField(label="Nº Booking:",  required=False)
    escritorio = forms.ModelChoiceField(queryset=Escritorio.objects.all().order_by('nome_escritorio'), label="Escritório:")
    pol = forms.CharField(label="Pol:",  required=False)
    pod = forms.CharField(label="Pod:",  required=False)
    navio = forms.CharField(label="Navio:",  required=False)
    eta = forms.DateField(widget=NumberInput(attrs={'type': 'date'}), label="Eta:",  required=False)
    armador = forms.CharField(label="Armador:",  required=False)
    commodity = forms.CharField(label="Commodity:",  required=False)
    quantidade = forms.DecimalField(label="Quantidade:",  required=False)
    type = forms.CharField(label="Type:",  required=False)
    shipper = forms.CharField(label="Shipper:",  required=False)
    cotacao = forms.CharField(label="Cotação:",  required=False)
    contrato_venda = forms.CharField(label="Contrato de Venda:",  required=False)

    #cadastrado_por = forms.ModelChoiceField(queryset=Funcionario.objects.all().order_by(), label="Quem Cadastrou?:")
    #vendido_por = forms.ModelChoiceField(queryset=Funcionario.objects.all().order_by(), label="Quem vendeu?:")

    observacoes = forms.CharField(widget=forms.Textarea(attrs={'rows':3}), label="Observações:", required=False)




class VenderBookingForm(forms.ModelForm):
    class Meta:
        model = Booking

        fields = ['shipper',
                  'contrato_venda',
                  'data_venda',
                  ]
        widgets = {
            'data_venda': forms.DateInput(
        attrs = {'type': 'date', 'class': 'form_input', 'value': date.today().strftime("%Y-%m-%d")}),
        }


    shipper = forms.CharField(label="Shipper")
    contrato_venda = forms.CharField(label="Contrato de Venda")
