from django.contrib import admin

from .models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    search_fields = ['name', 'ville', 'codePostal']
    list_filter = ['ville']
    list_display = ['name', 'adresse', 'ville', 'phone', 'website']
    ordering = ['name']
    list_per_page = 10


