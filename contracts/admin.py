# Register your models here.

from django.contrib import admin
from .models import Contract

class ListContracts(admin.ModelAdmin):
    list_display = ('id', 'name', 'email','role', 'company')
    list_display_links = ('name', 'email') 
    search_fields = ('name', )
    list_per_page = 10

admin.site.register(Contract, ListContracts)