from django.urls import path
from .views import Index
from ..controle_vazios.views import ExportarCSV
from .views import  login_user, submit_login, logout_user



urlpatterns = [
    path('', Index),
    path('login/', login_user),
    path('logout/', logout_user),
    path('login/submit', submit_login),

    path('exportar-csv/', ExportarCSV)

]