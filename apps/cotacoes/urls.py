from django.urls import path
from .views import Index
from .views import CadastrarCotacoes


urlpatterns = [
    path('', Index),
    path('cadastrar-cotacoes/', CadastrarCotacoes.as_view(), name='cadastrar-cotacoes'),




]