from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView
from django.db.models import F, Q
from django.http import HttpResponse
import csv
from datetime import datetime, date, timedelta
from django.core.paginator import Paginator



from .models import Booking
from .forms import VenderBookingForm, CadastrarBookingForm, EditarBookingForm


# Create your views here.
@login_required(login_url='/login/')
def Index(request):
    bookings = Booking.objects.all()
    queryset = request.GET.get('q')
    if queryset:
        bookings = Booking.objects.filter(
            Q(number_booking__icontains=queryset))

    return render (request, 'booking/index.html', {'bookings': bookings})


class BookingCreate(SuccessMessageMixin,CreateView):
    today = date.today()
    model = Booking
    form_class = CadastrarBookingForm
    template_name = 'booking/cadastrar-booking.html'
    success_url = '/'
    success_message = 'Booking Cadastrado com sucesso!!!!'



    def form_valid(self, form):
        form.instance.status = 'Vazio'
        form.instance.cadastrado_por = self.request.user
        return super(BookingCreate, self).form_valid(form)




@login_required(login_url='/login/')
def EditarBookingDisponivel(request, id=None):
    booking = get_object_or_404(Booking, id=id)
    form = EditarBookingForm(request.POST or None, instance=booking)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'Booking editado com sucesso.')
        return redirect('/')
    return render(request, 'booking/editar-booking-disponivel.html', {'form': form})


@login_required(login_url='/login/')
def ListaBookingDisponivel(request):
    from django.db.models.functions import ExtractDay
    from django.db.models import F, Func
    from django.db.models import Avg, F
    if request.user.funcionario.escritorio:
        bookings = Booking.objects.filter(status='Vazio').filter(escritorio=request.user.funcionario.escritorio).annotate(
    duration = Func(F('eta'), F('data_ddl_draft'), function='age')
).filter(duration__gt=timedelta(days=365))

        queryset = request.GET.get('q')
        if queryset:
            bookings = Booking.objects.filter(
                Q(number_booking__icontains=queryset)).filter(status='Vazio')
    else:
        bookings = Booking.objects.filter(status='Vazio')
        queryset = request.GET.get('q')
        if queryset:
            bookings = Booking.objects.filter(
                Q(number_booking__icontains=queryset)).filter(status='Vazio')

    paginator = Paginator(bookings, 10)  # Show 25 contacts per page

    page = request.GET.get('page')
    bookings = paginator.get_page(page)


    return render (request, 'booking/lista-booking-disponivel.html', {'bookings': bookings})


@login_required(login_url='/login/')
def RemoverBookingDisponivel(request, id=None):
    booking = get_object_or_404(Booking, id=id)
    if request.method == "POST":
        booking.delete()
        messages.success(request, 'Booking removido com sucesso!')
        return redirect('/booking/lista-booking-disponivel/')
    return render(request, 'booking/deletar-booking-disponivel.html', {'booking': booking})


@login_required(login_url='/login/')
def ListaBookingVendido(request):
    #Exibi a lista com apenas os bookings da filial do funcionario )
    if request.user.funcionario.escritorio:
        bookings = Booking.objects.filter(status='Vendido').filter(escritorio=request.user.funcionario.escritorio)
        queryset = request.GET.get('q')
        if queryset:
            bookings = Booking.objects.filter(
                Q(number_booking__icontains=queryset)).filter(status='Vendido')
    #Exibi a lista contendo todos os bookings            
    else:
        bookings = Booking.objects.filter(status='Vendido')
        queryset = request.GET.get('q')
        if queryset:
            bookings = Booking.objects.filter(
                Q(number_booking__icontains=queryset)).filter(status='Vendido')
    return render (request, 'booking/lista-booking-vendido.html', {'bookings': bookings})


@login_required(login_url='/login/')
def RemoverBookingVendido(request, id=None):
    booking = get_object_or_404(Booking, id=id)
    if request.method == "POST":
        booking.delete()
        messages.success(request, 'Booking removido com sucesso!')
        return redirect('/booking/lista-booking-vendido/')
    return render(request, 'booking/deletar-booking-vendido.html', {'booking': booking})


@login_required(login_url='/login/')
def VenderBooking(request, id=None):
    booking = get_object_or_404(Booking, id=id)
    form = VenderBookingForm(request.POST or None, instance=booking)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.status = 'Vendido'
        obj.vendido_por = request.user
        obj.save()
        messages.success(request, 'Booking vendido com sucesso')
        return redirect('/')
    return render(request, 'booking/vender-booking.html', {'form': form})


@login_required(login_url='/login/')
def EditarBookingVendido(request, id=None):
    booking = get_object_or_404(Booking, id=id)
    form = CadastrarBookingForm(request.POST or None, instance=booking)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'Booking editado com sucesso.')
        return redirect('/')
    return render(request, 'booking/editar-booking-vendido.html', {'form': form})


@login_required(login_url='/login/')
def VisualizarBookingVendido(request):
    booking = request.GET.get('id')
    if booking:
        booking = Booking.objects.get(id=booking)
    return render(request, 'booking/visualizar-booking-vendido.html',{'booking': booking})


@login_required(login_url='/login/')
def VisualizarBookingDisponivel(request):
    booking = request.GET.get('id')
    if booking:
        booking = Booking.objects.get(id=booking)
    return render(request, 'booking/visualizar-booking-disponivel.html',{'booking': booking})



def ExportarCSV(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="relatorio-booking.csv"'

    bookings = Booking.objects.filter(escritorio=request.user.funcionario.escritorio)

    writer = csv.writer(response)
    writer.writerow(['id','number_booking','pol','pod','navio','commodity','eta','armador','quantidade','type','status',
                     'cotacao','shipper','contrato_venda','cadastrado_por','data_cadastro','vendido_por','data_venda',
                     'escritorio','data_ddl_draft','hora_ddl_draft','observacoes'
                     ])
    for booking in bookings:
        writer.writerow([booking.id ,booking.number_booking,booking.pol,booking.pod,booking.navio,booking.commodity,
                         booking.eta ,booking.armador, booking.quantidade, booking.type, booking.status, booking.cotacao,
                         booking.shipper, booking.contrato_venda, booking.cadastrado_por, booking.data_cadastro,
                         booking.vendido_por, booking.data_venda, booking.escritorio,booking.data_ddl_draft,
                         booking.hora_ddl_draft ,booking.observacoes
                         ])
    return response