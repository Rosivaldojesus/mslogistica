from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from ..booking.models import Booking


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
    quantidade_boooking_disponivel = Booking.objects.filter(status='Vazio').count()
    quantidade_boooking_vendido = Booking.objects.filter(status='Vendido').count()
    return render(request, 'core/index.html', {
        'quantidade_boooking_disponivel':quantidade_boooking_disponivel,
        'quantidade_boooking_vendido': quantidade_boooking_vendido
        })



from django.contrib.admin.models import LogEntry, ADDITION
def Logs(request):
    logs = LogEntry.objects.all()
    return render(request, 'core/logs.html', {'logs': logs})
