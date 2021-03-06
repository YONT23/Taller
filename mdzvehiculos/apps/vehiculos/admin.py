from django.contrib import admin
from apps.vehiculos.models import Vehiculo, Marca, TipoVehiculo

# Register your models here.

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'color', 'placa','motor','marca','tipovehiculo')
    ordering = ('modelo', 'color', 'placa','motor','marca','tipovehiculo')
    search_fields = ('marca__nombre','modelo','tipovehiculo__nombre')
    list_filter = ('marca__nombre','modelo','tipovehiculo',)

admin.site.register(TipoVehiculo)
admin.site.register(Marca)
admin.site.register(Vehiculo, VehiculoAdmin)