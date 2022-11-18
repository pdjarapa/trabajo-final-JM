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

class EjecucionPruebaAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['comentario'].widget = forms.widgets.Textarea(attrs={'cols': 40, 'rows': 3})

    class Meta:
        fields = '__all__'
        model = EjecucionPrueba

class EjecucionPruebaInline(admin.TabularInline):
    model = EjecucionPrueba
    extra = 0
    form = EjecucionPruebaAdminForm

    def get_formset(self, request, obj=None, **kwargs):
        formset = super(EjecucionPruebaInline, self).get_formset(request, obj, **kwargs)
        print('proyecto:::', type(obj))
        if type(obj) == Proyecto:
            formset.form.base_fields["ciclo_prueba"].queryset = formset.form.base_fields["ciclo_prueba"].queryset.filter(proyecto=obj)
            formset.form.base_fields["caso_prueba"].queryset = formset.form.base_fields["caso_prueba"].queryset.filter(proyecto=obj)

        #if type(obj) == CicloPrueba:
        #    formset.form.base_fields["ciclo_prueba"].queryset = formset.form.base_fields["ciclo_prueba"].queryset.filter(proyecto=obj.proyecto)
        #    formset.form.base_fields["caso_prueba"].queryset = formset.form.base_fields["caso_prueba"].queryset.filter(proyecto=obj.proyecto)

        return formset
