from django.urls import path
from .views import Index, VazioDisponivel
from .views import CadastrarVazio, VenderVazio, VazioDisponivel, VazioVendido



urlpatterns = [
    path('', Index),
    path('vender-vazio/<int:id>', VenderVazio),
    path('vazio-disponivel/', VazioDisponivel),
    path('vazio-vendido/', VazioVendido),

    path('cadastrar-vazio/', CadastrarVazio.as_view(), name='cadastrar-vazio'),


]