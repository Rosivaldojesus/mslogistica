from django.urls import path
from .views import Index
from .views import CadastrarVazio



urlpatterns = [
    path('', Index),

    path('cadastrar-vazio/', CadastrarVazio.as_view(), name='cadastrar-vazio'),

]