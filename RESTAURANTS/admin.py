from django.contrib import admin

from .models import Restaurant


# admin.site.register(Restaurant)


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    search_fields = ['name', 'ville']
    list_filter = ['ville']
