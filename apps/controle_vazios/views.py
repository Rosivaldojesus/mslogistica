from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic.edit import CreateView
from .models import ControleVazios
from .forms import ControleVaziosForm, VenderVaziosForm

# Create your views here.

def Index(request):
    vazios = ControleVazios.objects.all()
    return render(request, 'controle_vazios/index.html', {'vazios':vazios})

def VazioDisponivel(request):
    vazios = ControleVazios.objects.filter(shipper__isnull=True).filter(contrato_venda__isnull=True)
    return render(request, 'controle_vazios/vazio-disponivel.html', {'vazios':vazios})

def VazioVendido(request):
    vazios = ControleVazios.objects.filter(shipper__isnull=False).filter(contrato_venda__isnull=False)
    return render(request, 'controle_vazios/vazio-vendido.html', {'vazios':vazios})


class CadastrarVazio(CreateView):
    model = ControleVazios
    form_class = ControleVaziosForm
    template_name = 'controle_vazios/cadastrar-vazio.html'
    success_url = '/controle-vazios/'


def VenderVazio(request, id=None):
    insta = get_object_or_404(ControleVazios, id=id)
    form = VenderVaziosForm(request.POST or None, instance=insta)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'Vazio vendido com sucesso')
        return redirect('/controle-vazios/')
    return render(request, 'controle_vazios/vender-vazio.html', {'form': form})