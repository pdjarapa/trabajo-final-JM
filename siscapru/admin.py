from django.contrib import admin

from siscapru.models import *


#Model Admins
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'activo')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('activo', )

# Register your models here.
admin.site.register(Proyecto, ProyectoAdmin)

admin.site.register(CasoPrueba)

admin.site.register(CicloPrueba)

admin.site.register(EjecucionPrueba)