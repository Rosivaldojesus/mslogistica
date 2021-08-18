from django.shortcuts import render
from ..controle_vazios.models import ControleVazios
from ..controle_fretes.models import ControleFretes

# Create your views here.

def Index(request):
    quant_fretes = ControleFretes.objects.all().count()
    quant_vazios = ControleVazios.objects.all().count()
    quant_vazios_disponiveis = ControleVazios.objects.filter(shipper__isnull=True).filter(contrato_venda__isnull=True).count()
    quant_vazios_vendidos = ControleVazios.objects.filter(shipper__isnull=False).filter(contrato_venda__isnull=False).count()


    return render(request, 'core/index.html', {
        'quant_vazios':quant_vazios, 'quant_fretes':quant_fretes,
        'quant_vazios_disponiveis':quant_vazios_disponiveis, 
        'quant_vazios_vendidos': quant_vazios_vendidos
        })
