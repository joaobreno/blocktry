from django.contrib import admin
from .models import Mail

class ListMail(admin.ModelAdmin):
    list_display = ('name', 'email','date')
    readonly_fields = ('name', 'email', 'phone', 'message', 'date')
    list_display_links = ('name', 'email') 
    search_fields = ('email', )
    list_per_page = 10

admin.site.register(Mail, ListMail)