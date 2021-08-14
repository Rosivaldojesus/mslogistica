from django.shortcuts import render
from .models import ControleFretes
from django.views.generic.edit import CreateView
from .forms import ControleFretesForm

# Create your views here.
def Index(request):
    fretes = ControleFretes.objects.all()
    return render(request, 'controle_fretes/index.html', {'fretes':fretes})


class CadastrarFrete(CreateView):
    model = ControleFretes
    form_class = ControleFretesForm
    template_name = 'controle_fretes/cadastrar-frete.html'
    success_url = '/controle-fretes/'