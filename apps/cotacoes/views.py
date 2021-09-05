from django.shortcuts import render
from .models import Cotacoes
from django.views.generic.edit import CreateView
from .forms import CotacoesForm

# Create your views here.
def Index(request):
    fretes = Cotacoes.objects.all()
    return render(request, 'cotacoes/index.html', {'fretes':fretes})


class CadastrarCotacoes(CreateView):
    model = Cotacoes
    form_class = CotacoesForm
    template_name = 'cotacoes/cadastrar-cotacoes.html'
    success_url = '/cotacoes/'