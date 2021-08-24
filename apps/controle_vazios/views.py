from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic.edit import CreateView
from .models import ControleVazios
from .forms import ControleVaziosForm, VenderVaziosForm
from django.db.models import F, Q
import csv
from django.http import HttpResponse

# Create your views here.

def Index(request):
    vazios = ControleVazios.objects.all()
    return render(request, 'controle_vazios/index.html', {'vazios':vazios})

def VazioDisponivel(request):
    quant_vazios_disponiveis = ControleVazios.objects.filter(status='Vazio').count()
    vazios = ControleVazios.objects.filter(status='Vazio')
    queryset = request.GET.get('q')
    if queryset:
        vazios = ControleVazios.objects.filter(
            Q(number_booking__icontains=queryset) |
            Q(pod__icontains=queryset)
            ).filter(status='Vazio')

    return render(request, 'controle_vazios/vazio-disponivel.html', {
        'vazios':vazios,
        'quant_vazios_disponiveis':quant_vazios_disponiveis,

    })




def VazioVendido(request):
    vazios = ControleVazios.objects.filter(status='Vendido')
    queryset = request.GET.get('q')
    if queryset:
        vazios = ControleVazios.objects.filter(
            Q(number_booking__icontains=queryset) |
            Q(pod__icontains=queryset)
        ).filter(status='Vendido')
    return render(request, 'controle_vazios/vazio-vendido.html', {'vazios':vazios})


class CadastrarVazio(CreateView):
    model = ControleVazios
    form_class = ControleVaziosForm
    template_name = 'controle_vazios/cadastrar-vazio.html'
    success_url = '/'


def VenderVazio(request, id=None):
    insta = get_object_or_404(ControleVazios, id=id)
    form = VenderVaziosForm(request.POST or None, instance=insta)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.status = 'Vendido'
        obj.save()
        messages.success(request, 'Vazio vendido com sucesso')
        return redirect('/')
    return render(request, 'controle_vazios/vender-vazio.html', {'form': form})


def VazioVisualizacao(request):
    vazio = request.GET.get('id')
    if vazio:
        vazio = ControleVazios.objects.get(id=vazio)
    return render(request, 'controle_vazios/visualizar-vazio.html',{'vazio': vazio})








def ExportarCSV(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="relatorio-vazios.csv"'

    vazios = ControleVazios.objects.all()

    writer = csv.writer(response)
    writer.writerow(['id', 'number_booking', 'pol', 'pod', 'navio',
                     'cmmdty', 'eta', 'armador','quantidade','type','status','cotacao','shipper','contrato_venda','observacoes',
                     ])
    for vazio in vazios:
        writer.writerow([vazio.id, vazio.number_booking, vazio.pol, vazio.pod, vazio.navio, vazio.cmmdty, vazio.eta,
                         vazio.armador, vazio.quantidade, vazio.type, vazio.status, vazio.cotacao, vazio.shipper,
                         vazio.contrato_venda, vazio.observacoes
                         ])

    return response