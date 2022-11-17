from django.contrib import admin
from django import forms
from siscapru.models import *

class CasoPruebaAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        attrs_txta = {'cols': 20, 'rows': 2}
        self.fields['descripcion'].widget = forms.widgets.Textarea(attrs=attrs_txta)
        self.fields['precondicion'].widget = forms.widgets.Textarea(attrs=attrs_txta)
        self.fields['pasos'].widget = forms.widgets.Textarea(attrs=attrs_txta)
        self.fields['resultado_esperado'].widget = forms.widgets.Textarea(attrs=attrs_txta)
        self.fields['postcondicion'].widget = forms.widgets.Textarea(attrs=attrs_txta)

    class Meta:
        fields = '__all__'
        model = CasoPrueba

class CasoPruebaInline(admin.TabularInline):
    model = CasoPrueba
    extra = 0
    form = CasoPruebaAdminForm
    #classes = ('collapse',)
    fieldsets = [
        ['Datos generales', {
            'classes': ['collapse'],
            'fields': [
                ('codigo', 'estado'),
                ('prioridad', 'tipo', 'variedad', 'evaluacion'),
                ('descripcion', ),
                ('precondicion', 'postcondicion', 'pasos', 'resultado_esperado'),
            ]
        }],
    ]


class CicloPruebaAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        attrs_txta = {'cols': 40, 'rows': 3}
        self.fields['nombre'].widget = forms.widgets.TextInput()
        self.fields['descripcion'].widget = forms.widgets.Textarea(attrs=attrs_txta)


    class Meta:
        fields = '__all__'
        model = CicloPrueba

class CicloPruebaInline(admin.TabularInline):
    model = CicloPrueba
    extra = 0
    form = CicloPruebaAdminForm
    show_change_link = True

class EjecucionPruebaInline(admin.TabularInline):
    model = EjecucionPrueba
