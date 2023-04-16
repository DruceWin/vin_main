from django.contrib import admin
from .models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'engine', 'gearbox', 'vin', 'is_hidden')
    search_fields = ('brand', 'model', 'vin')


admin.site.register(Car, CarAdmin)
