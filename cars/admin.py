from django.contrib import admin
from .models import Car, Photos


class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'engine', 'gearbox', 'vin')
    search_fields = ('brand', 'model', 'vin')


admin.site.register(Car, CarAdmin)


admin.site.register(Photos)
