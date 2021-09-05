from django.contrib import admin
from .models import Funcionario

# Register your models here.

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome','user')
    list_filter = ('nome','user')
    search_fields = ('nome', 'user')
    list_display_links =  ('nome', 'user')

admin.site.register(Funcionario, FuncionarioAdmin)
