from django.contrib import admin
from .models import Booking

# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'number_booking','pol','pod','navio','status',)
    list_filter = ('number_booking','status',)
    search_fields = ('number_booking','pol','pod','navio', )
    list_display_links =  ('number_booking','pol','pod','navio','status',)


admin.site.register(Booking, BookingAdmin)
