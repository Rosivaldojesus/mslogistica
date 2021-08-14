from django.shortcuts import render
from ..controle_vazios.models import ControleVazios
from ..controle_fretes.models import ControleFretes

# Create your views here.

def Index(request):
    quant_fretes = ControleFretes.objects.all().count()
    quant_vazios = ControleVazios.objects.all().count()
    return render(request, 'core/index.html', {
        'quant_vazios':quant_vazios, 'quant_fretes':quant_fretes})
