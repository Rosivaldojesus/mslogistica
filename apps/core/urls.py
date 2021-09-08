from django.urls import path
from .views import Index

from .views import  login_user, submit_login, logout_user, Logs



urlpatterns = [
    path('', Index),
    path('login/', login_user),
    path('logout/', logout_user),
    path('login/submit', submit_login),
    path('logs', Logs),

]