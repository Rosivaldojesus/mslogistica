from django.contrib import admin
from .models import Booking

# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'number_booking','status','escritorio')
    list_filter = ('number_booking','status','escritorio')
    search_fields = ('number_booking', 'escritorio')
    list_display_links =  ('number_booking','status','escritorio')


admin.site.register(Booking, BookingAdmin)
