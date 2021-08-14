from django.urls import path
from .views import Index
from .views import CadastrarFrete


urlpatterns = [
    path('', Index),
    path('cadastrar-frete/', CadastrarFrete.as_view(), name='cadastrar-frete'),




]