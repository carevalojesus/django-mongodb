from django.contrib import admin
from .models import Categoria, Transaccion

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')

@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'categoria', 'monto', 'fecha', 'fecha_creacion', 'fecha_modificacion')
    list_filter = ('tipo', 'categoria', 'fecha')
    search_fields = ('tipo', 'categoria__nombre', 'monto', 'descripcion')
    date_hierarchy = 'fecha'
    ordering = ('-fecha', 'fecha_creacion')
    list_per_page = 20

