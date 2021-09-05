from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from ..booking.models import Booking


from ..controle_vazios.models import ControleVazios
from ..controle_fretes.models import ControleFretes

# Create your views here.
def login_user(request):
    return render(request, 'core/login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Por favor, insira um usuário e senha corretos para uma conta de equipe."
             "Note que ambos campos são sensíveis a maiúsculas e minúsculas.")
    return redirect('/')


@login_required(login_url='/login/')
def Index(request):
    quant_fretes = ControleFretes.objects.all().count()
    quant_vazios = ControleVazios.objects.all().count()


    quantidade_boooking_disponivel = Booking.objects.filter(status='Vazio').count()
    quantidade_boooking_vendido = Booking.objects.filter(status='Vendido').count()

    return render(request, 'core/index.html', {
        'quant_vazios':quant_vazios, 'quant_fretes':quant_fretes,
        'quantidade_boooking_disponivel':quantidade_boooking_disponivel,
        'quantidade_boooking_vendido': quantidade_boooking_vendido
        })
