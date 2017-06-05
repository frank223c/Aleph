#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from .models import *
from django.forms.extras.widgets import SelectDateWidget
from datetime import datetime, timedelta, date
from django.utils.translation import ugettext, ugettext_lazy as _
from django.conf import settings
from django.contrib.admin import widgets   
from django.forms import ValidationError
from .widgets import *
from django.utils import timezone
from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import TabHolder, Tab
from django.forms.fields import DateField 
from django.contrib.admin.widgets import AdminDateWidget 

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

#Formulario de arqueologia utilizando los widgets personalizados
class ArqueologiaForm(forms.ModelForm): 
    class Meta:
      model = Arqueologia
      widgets = {
            'seccion': SelectWithPop(attrs={'cols': 80, 'rows': 20}),
            'ubicacion': SelectWithPop(attrs={'cols': 80, 'rows': 20}),
            'bibliografia': MultipleSelectWithPop(attrs={'cols': 80, 'rows': 20}),
            'serie': SelectWithPop(attrs={'cols': 80, 'rows': 20}),
            'yacimiento': SelectWithPop(attrs={'cols': 80, 'rows': 20}),
            'cultura': SelectWithPop(attrs={'cols': 80, 'rows': 20}),
            'material': MultipleSelectWithPop(attrs={'cols': 80, 'rows': 20}),
                        
           # 'movimiento': MultipleSelectWithPop(attrs={'cols': 80, 'rows': 20}),
        }
      fields = "__all__"
      
      def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(ArqueologiaForm, self).__init__(*args, **kwargs)
        self.fields["material"].widget = Textarea()
        self.fields["bibliografia"].widget = Textarea()
        
      def clean_material(self):
          data = self.cleaned_data.get('material')
          return data.split(',') # 
          
      def clean_bibliografia(self):
          data = self.cleaned_data.get('bibliografia')
          # validamos los datos y lso convertimos en una cadena
          # ya que se espera una lista
          # si no es valido recibiremos un error
          return data.split(',') # funcion para trocear los datos y pasarlo como una lista de valores separados por una coma

   
      
#Datos alojados en tablas externas que se crean mediante un pop-up 
class BibliografiaForm(forms.ModelForm):
    class Meta:
       model = Bibliografia
       fields = "__all__"

class MovimientoForm(forms.ModelForm):
    class Meta:
       model = Movimiento
       fields = "__all__"

class EstudioForm(forms.ModelForm):
    class Meta:
       model = Estudio
       fields = "__all__"
       
       
#Formulario de datos especificos de cada categoria
      
#Adición de datos mediante pop-ups mediante el widget creado para arqueologia

class MaterialForm(forms.ModelForm):
    class Meta:
       model = Material
       fields = "__all__"

class SeccionForm(forms.ModelForm):
    class Meta:
       model = Seccion
       fields = "__all__"

class SerieForm(forms.ModelForm):
    class Meta:
       model = Serie
       fields = "__all__"

class CulturaForm(forms.ModelForm):
    class Meta:
       model = Cultura
       fields = "__all__"       

class YacimientoForm(forms.ModelForm):
    class Meta:
       model = Yacimiento
       fields = "__all__"
       
#Creacion del formulario especifico de bellas artes

class BellasArtesForm(forms.ModelForm):   
   class Meta:
       model = Bellasartes
       widgets = {
            'ubicacion': SelectWithPop(attrs={'cols': 80, 'rows': 20}),
            'bibliografia': MultipleSelectWithPop(attrs={'cols': 80, 'rows': 20}),
            'tecnica': MultipleSelectWithPop(attrs={'cols': 80, 'rows': 20}),
            'autor': SelectWithPop(attrs={'cols': 80, 'rows': 20}),
            'soporte': MultipleSelectWithPop(attrs={'cols': 80, 'rows': 20}),
            'tecnica': MultipleSelectWithPop(attrs={'cols': 80, 'rows': 20}),
            'movimientos': MultipleSelectWithPop(attrs={'cols': 80, 'rows': 20}),
            'donante': SelectWithPop(attrs={'cols': 80, 'rows': 20}),
            'contexto': SelectWithPop(attrs={'cols': 80, 'rows': 20}),
            'estilo': SelectWithPop(attrs={'cols': 80, 'rows': 20}),
            'iconografia': SelectWithPop(attrs={'cols': 80, 'rows': 20}),
        }
       fields = "__all__"
       
       def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(ArqueologiaForm, self).__init__(*args, **kwargs)
        self.fields["soporte"].widget = Textarea()
        self.fields["tecnica"].widget = Textarea()
        self.fields["bibliografia"].widget = Textarea()
        
       def clean_tecnica(self):
          data = self.cleaned_data.get('tecnica')
          return data.split(',') # just an exa
          
       def clean_soporte(self):
          data = self.cleaned_data.get('soporte')
          return data.split(',') # just an exa
          
       def clean_bibliografia(self):
          data = self.cleaned_data.get('bibliografia')
          # validamos los datos y lso convertimos en una cadena
          # ya que se espera una lista
          # si no es valido recibiremos un error
          return data.split(',') # funcion para trocear los datos y pasarlo como una lista de valores separados por una coma


class AutorForm(forms.ModelForm):
    class Meta:
       model = Autor
       fields = "__all__"

class SoporteForm(forms.ModelForm):
    class Meta:
       model = Soporte
       fields = "__all__"

class TecnicaForm(forms.ModelForm):
    class Meta:
       model = Tecnica
       fields = "__all__"


class DonanteForm(forms.ModelForm):
    class Meta:
       model = Donante
       fields = [ "nombre","apellidos","dni"]

    def cleandni(self):
      diccionario_limpio = self.cleaned_data
      dni = diccionario_limpio.get('dni')

      if len(dni) != 9:
         raise forms.ValidationError("No es un DNI válido,compruebe los espacios")
      return dni

#
# INTERVENCIONES
#

class InformeEstadoForm(forms.ModelForm):
   objeto = forms.ModelChoiceField(queryset=Objeto.objects.all(),widget=forms.TextInput(attrs={'readonly':'readonly'}))
   fecha = forms.DateField(widget = SelectDateWidget)

   class Meta:
       model = InformeEstado
       widgets = {
            'estudio': MultipleSelectWithPop(attrs={'cols': 80, 'rows': 20})
            }
       fields = "__all__"
       def __init__(self, *args, **kwargs):
         self.request = kwargs.pop('request')
         super(EstadoForm, self).__init__(*args, **kwargs)
         self.fields["estudio"].widget = Textarea()
        
       def clean_estudios(self):
           data = self.cleaned_data.get('estudio')
           return data.split(',')

class InformeArqueoForm(forms.ModelForm):
  objeto = forms.ModelChoiceField(queryset=Objeto.objects.all(),widget=forms.TextInput(attrs={'readonly':'readonly'}))
  class Meta:
      model = InformeArqueo 
      fields = "__all__"


class IntervencionForm(forms.ModelForm):
    estado_rel = forms.ModelChoiceField(queryset=InformeEstado.objects.all(),widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
       model = InformeIntervencion
       fields = "__all__"

class IconografiaForm(forms.ModelForm):
    class Meta:
       model = Iconografia
       fields = "__all__"
