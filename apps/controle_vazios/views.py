from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import ControleVazios
from .forms import ControleVaziosForm

# Create your views here.

def Index(request):
    vazios = ControleVazios.objects.all()
    return render(request, 'controle_vazios/index.html', {'vazios':vazios})

class CadastrarVazio(CreateView):
    model = ControleVazios
    form_class = ControleVaziosForm
    template_name = 'controle_vazios/cadastrar-vazio.html'
    success_url = '/controle-vazios/'