from django.contrib import admin
from siscapru.forms import CasoPruebaInline, CicloPruebaInline, EjecucionPruebaInline, CasoPruebaAdminForm, \
    EjecucionPruebaAdminForm, CicloPruebaAdminForm
from siscapru.models import *

admin.site.site_header = 'Gestión Casos Prueba'
admin.site.index_title = 'Panel de control'
admin.site.site_title = 'Sgcp'

#Model Admins
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'casos_prueba', 'ciclos_prueba', 'activo')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('activo', )
    inlines = [CasoPruebaInline, CicloPruebaInline]

    @admin.display(empty_value='???')
    def casos_prueba(self, obj):
        return obj.casos_prueba.count()

    @admin.display(empty_value='???')
    def ciclos_prueba(self, obj):
        return obj.ciclos_prueba.count()

class CasoPruebaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion', 'estado')
    #search_fields = ('nombre', 'descripcion')
    list_filter = ('proyecto', )
    raw_id_fields = ('proyecto',)
    form = CasoPruebaAdminForm

class CicloPruebaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'proyecto')
    #search_fields = ('nombre', 'descripcion')
    list_filter = ('proyecto', )
    inlines = [EjecucionPruebaInline]
    form = CicloPruebaAdminForm


class EjecucinPruebaAdmin(admin.ModelAdmin):
    list_display = ('ciclo_prueba', 'caso_prueba', 'get_proyecto')
    #search_fields = ('nombre', 'descripcion')
    list_filter = ('ciclo_prueba__proyecto', 'estado',)
    form = EjecucionPruebaAdminForm

# Register your models here.
admin.site.register(Proyecto, ProyectoAdmin)

admin.site.register(CasoPrueba, CasoPruebaAdmin)

admin.site.register(CicloPrueba, CicloPruebaAdmin)

# no admin
#admin.site.register(EjecucionPrueba, EjecucinPruebaAdmin)