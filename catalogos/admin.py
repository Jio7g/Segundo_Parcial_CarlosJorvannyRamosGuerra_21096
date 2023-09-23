from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['dni', 'nombre', 'direccion', 'fecha_nacimiento']
    search_fields = ['dni', 'nombre', 'direccion']
    list_filter = ['fecha_nacimiento', 'direccion']

