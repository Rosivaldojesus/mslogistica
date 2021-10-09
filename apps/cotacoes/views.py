from django.shortcuts import render, redirect , get_object_or_404
from .models import Cotacoes
from django.views.generic.edit import CreateView
from .forms import CotacoesForm, EditarCotacoesForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def Index(request):
    fretes = Cotacoes.objects.all()
    return render(request, 'cotacoes/index.html', {'fretes':fretes})


class CadastrarCotacoes(CreateView):
    model = Cotacoes
    form_class = CotacoesForm
    template_name = 'cotacoes/cadastrar-cotacoes.html'
    success_url = '/cotacoes/'



@login_required(login_url='/login/')
def EditarCotacoes(request, id=None):
    cotacoes = get_object_or_404(Cotacoes, id=id)
    form = EditarCotacoesForm(request.POST or None, instance=cotacoes)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'Cotação editado com sucesso.')
        return redirect('/')
    return render(request, 'cotacoes/editar-cotacoes.html', {'form': form})


@login_required(login_url='/login/')
def CotacaoVisualizacao(request):
    cotacao = request.GET.get('id')
    if cotacao:
        cotacao = Cotacoes.objects.get(id=cotacao)
    return render(request, 'cotacoes/visualizar-cotacao.html',{'cotacao': cotacao})