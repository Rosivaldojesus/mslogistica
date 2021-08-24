from django.urls import path
from .views import Index
from ..controle_vazios.views import ExportarCSV



urlpatterns = [
    path('', Index),

    path('exportar-csv/', ExportarCSV)

]