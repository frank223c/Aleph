# -*- encoding: utf-8 -*
from django.contrib import admin
# Register your models here.
from .models import *
from bug.models import *

class AdminArqueologia(admin.ModelAdmin):
 list_display = ["nombre","seccion","edad"]
 list_filter = ["seccion"]
 #list_editable = ["numinv","nombre","edad"]
 search_fields = ["numinv","nombre","seccion","edad","material"]
 
 class Meta:
     model = Arqueologia
     
     
class AdminArte(admin.ModelAdmin):
 list_display = ["numinv","titulo","autor","ubicacionmus","formaingreso"]
 list_display_links =["numinv"]
 list_filter = ["autor"]
 list_editable = ["titulo","ubicacionmus"]
 search_fields = ["numinv","titulo","autor","fechaingreso","ubicacionmus"]
 
        
 class Meta:
     model = Bellasartes
     
     
class AdminAutor(admin.ModelAdmin):
 list_display = ["nombre","apellidos","alias","fnac","fdef","procedencia"]
 list_filter = ["nombre"]
 list_editable = ["apellidos","alias"]
 search_fields = ["nombre","alias","apellido"]
      
 class Meta:
     model = Autor 

class AdminBibliografia(admin.ModelAdmin):
 list_display = ["autor","anio","pagina","isbn","edicion","url"]
 list_filter = ["autor","anio"]
 list_editable = ["url"]
 search_fields = ["anio","isbn","edicion"]
      
 class Meta:
     model = Bibliografia 


admin.site.register(Movimiento)
admin.site.register(Bibliografia,AdminBibliografia)
admin.site.register(Serie)
admin.site.register(Seccion)
admin.site.register(Cultura)
admin.site.register(Arqueologia,AdminArqueologia)
admin.site.register(Tecnica)
admin.site.register(Soporte)
admin.site.register(Bellasartes,AdminArte)
admin.site.register(Donante)
admin.site.register(Material)
admin.site.register(Yacimiento)
admin.site.register(Objeto)
admin.site.register(Estudio)
admin.site.register(InformeEstado)
admin.site.register(InformeIntervencion)
admin.site.register(InformeArqueo)
admin.site.register(Iconografia)
admin.site.register(Autor,AdminAutor)
