from django.contrib import admin
from django import forms
from siscapru.models import *

class CasoPruebaAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['descripcion'].widget = forms.widgets.Textarea(attrs={'cols': 30})
        self.fields['precondicion'].widget = forms.widgets.Textarea(attrs={'cols': 30})
        self.fields['pasos'].widget = forms.widgets.Textarea(attrs={'cols': 30})
        self.fields['resultado_esperado'].widget = forms.widgets.Textarea(attrs={'cols': 30})
        self.fields['postcondicion'].widget = forms.widgets.Textarea(attrs={'cols': 30})
        self.fields['observacion'].widget = forms.widgets.Textarea(attrs={'cols': 30})

    class Meta:
        fields = '__all__'
        model = CasoPrueba

#class CasoPruebaInline(admin.TabularInline):
class CasoPruebaInline(admin.StackedInline):
    model = CasoPrueba
    extra = 1
    form = CasoPruebaAdminForm
    #raw_id_fields = ('usuario', 'fase', 'tramite')

#Model Admins
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'activo')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('activo', )
    inlines = [CasoPruebaInline]


# Register your models here.
admin.site.register(Proyecto, ProyectoAdmin)

admin.site.register(CasoPrueba)

admin.site.register(CicloPrueba)

admin.site.register(EjecucionPrueba)