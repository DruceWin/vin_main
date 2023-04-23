from django.contrib import admin
from .models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'engine', 'gearbox', 'vin', 'is_hidden', 'is_hidden_v2')
    search_fields = ('brand', 'model', 'vin')
    ordering = ('-id', )


admin.site.register(Car, CarAdmin)
