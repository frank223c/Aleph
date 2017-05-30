# -*- encoding: utf-8 -*
from django.contrib import admin
# Register your models here.
from .models import *

class AdminArqueologia(admin.ModelAdmin):
 list_display = ["numinv","nombre","seccion","edad","yacimiento","conservacion","depositado","ubicacion"]
 list_display_links =["numinv"]
 list_filter = ["seccion"]
 list_editable = ["nombre","ubicacion","conservacion","edad"]
 search_fields = ["numinv","nombre","seccion","edad","material","fechaingreso","ubicacion"]
 
        
 class Meta:
     model = Arqueologia
     
     
class AdminArte(admin.ModelAdmin):
 list_display = ["numinv","titulo","autor","ubicacion","formaingreso"]
 list_display_links =["numinv"]
 list_filter = ["autor"]
 list_editable = ["titulo","ubicacion"]
 search_fields = ["numinv","titulo","autor","fechaingreso","ubicacion"]
 
        
 class Meta:
     model = Bellasartes
     
     
class AdminAutor(admin.ModelAdmin):
 list_display = ["nombre","apellidos","alias","fnac","fdef","procedencia","refbiografia"]
 list_filter = ["nombre"]
 list_editable = ["apellidos","alias","refbiografia"]
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


     
#~ class InformeIntervencion(admin.ModelAdmin):
 #~ list_display = ["numinv","nombre_restaurador","ape_restaurador","fecha","estudios","prioridad"]
 #~ list_filter = ["numinv","fecha"]
 #~ list_editable = ["","",""]
 #~ search_fields = ["","",""]
      
 #~ class Meta:
     #~ model = Autor  


admin.site.register(Ubicacion)
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
admin.site.register(Iconografia)
admin.site.register(Autor,AdminAutor)
