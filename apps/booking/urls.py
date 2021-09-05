from django.urls import path
from .views import Index, BookingCreate

from.views import ListaBookingDisponivel, EditarBookingDisponivel, VenderBooking, VisualizarBookingDisponivel, RemoverBookingDisponivel

from.views import ListaBookingVendido, EditarBookingVendido, VisualizarBookingVendido,  RemoverBookingVendido


urlpatterns = [
    path('', Index),
    path('lista-booking-disponivel/', ListaBookingDisponivel),
    path('editar-booking-disponivel/<int:id>', EditarBookingDisponivel),
    path('deletar-booking-disponivel/<int:id>', RemoverBookingDisponivel),
    path('lista-booking-vendido/', ListaBookingVendido),
    path('visualizar-booking-vendido/', VisualizarBookingVendido),
    path('visualizar-booking-disponivel/', VisualizarBookingDisponivel),
    path('vender-booking/<int:id>', VenderBooking),
    path('deletar-booking-vendido/<int:id>', RemoverBookingVendido),

    path('editar-booking-vendido/<int:id>', EditarBookingVendido),

    path('cadastrar-booking/', BookingCreate.as_view(), name='cadastrar-booking'),


]