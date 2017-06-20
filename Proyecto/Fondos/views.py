#!/usr/bin/env python
# -*- coding: utf-8 -*
from django.core.exceptions import PermissionDenied
from .models import *
from .forms import *
from django.utils.html import escape
from django.core.urlresolvers import reverse
from .filters import ArqueologiaFilter,BellasArtesFilter
from django.contrib.admin import widgets   
from django.conf import settings
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse 
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from django import http
from django.template.loader import get_template
from django.template import RequestContext
from django.template import Context
from django.contrib import auth
from django.contrib.auth.models import User
from funcionpermisos import group_required
from django.views.decorators.debug import sensitive_post_parameters


'''
VISTA DE LOGIN Y DEL INDEX, EL ADMINISTRADOR DE LA APLICACIÓN
SERÁ REDIRIGIDO A LA INTERFAZ DE ADMINISTRACIÓN, MIENTRAS QUE CADA
USUARIO DEPENDIENDO DE SU ROL, VERÁ LOS ÚLTIMOS DATOS INSERTADOS
QUE ESTÉN RELACIONADOS CON EL MISMO
'''

@sensitive_post_parameters()
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Contraseña correcta y usuario activo
        auth.login(request, user)
        return HttpResponseRedirect("/account/loggedin/")
    else:
        # Muestra pagina de error
        return HttpResponseRedirect("/account/invalid/")

@login_required
def index(request):
    if request.user.is_superuser:
      return HttpResponseRedirect("/admin/")
    else:
       group_name = request.user.groups.all()[0].name
       if group_name == "Documentador":
         ultimosarqueo = Arqueologia.objects.all().order_by('-fechaingreso')[:5]
         ultimosba = Bellasartes.objects.all().order_by('-fechaingreso')[:5]
         return render(request, "homedocu.html",{ "ultimosarqueo":ultimosarqueo,"ultimosba":ultimosba })
       if group_name == "RestauradorBA":
         ultimosinfo = InformeEstado.objects.all().order_by('-fecha')[:3]
         return render(request, "homerestauba.html", { "ultimosinfo":ultimosinfo })
       if group_name == "RestauradorARQ": 
         ultimosinfo = InformeArqueo.objects.all().order_by('-fecha')[:3]
         return render(request, "homerestauar.html",{ "ultimosinfo":ultimosinfo })         
  
def error(request):
     return render(request, "error.html")
     
'''
INSERCIÓN DE DATOS EN LA BASE DE DATOS
REALIZADO POR EL USUARIO CON EL ROL
DE DOCUMENTADOR
'''

#En el caso de las vistas de creación, si el método es POST
#se insertarán los datos en la BBDD, en caso contrario, como puede ser
#que el formulario no sea válido, se informará de errores al usuario
#como por ejemplo dejar campos requeridos vacíos y se volverá a mostrar
#el formulario 

@group_required('Documentador')
def arqueologia_crear(request): 
         if request.method == "POST":
            form = ArqueologiaForm(request.POST,request.FILES)    
            if form.is_valid():
              instance = form.save()
              instance.user = request.user 
              instance.save()
              messages.success(request, 'Acción realizada con éxito')
              return HttpResponseRedirect(instance.get_absolute_url())
         else:
             form = ArqueologiaForm()
         return render(request, "formularios/formulario_arqueologia.html", {"form": form})

@group_required('Documentador')
def bellasartes_crear(request):
         if request.method == "POST":
            form = BellasArtesForm(request.POST,request.FILES)    
            if form.is_valid():
              instance = form.save()
              instance.user = request.user 
              instance.save()
              messages.success(request, 'Acción realizada con éxito')
              return redirect('/')
         else:
              form = BellasArtesForm()
         return render(request,'formularios/formulario_bellasartes.html', {'form': form})

@group_required('RestauradorBA')
def estado_crear(request, pk):
    instance = get_object_or_404(Objeto, pk=pk)
    datos =  Objeto.objects.filter().get(pk=instance.id)
    datadict = {'objeto': datos.pk }
    if request.method == "POST":
      form = InformeEstadoForm(request.POST, initial=datadict)  
    #le pasamos el id del objeto mediante un diccionario inicial al formulario
    #de estado, de manera que el dato con el cual se relaciona la clase
    #informes estado no haya que rellenarlo    
      if form.is_valid():
          instance = form.save()
          instance.user = request.user
          instance.save()
          messages.success(request, 'Acción realizada con éxito')
          return redirect('/')#si el formulario es valido se registra el objeto, que sera visible tanto desde el admin como desde
    else:
         form = InformeEstadoForm(initial=datadict) 
    return render(request, "Informes/formulario_estado.html", {"form": form, "instance": instance, "datos": datos})



#En el caso de las intervenciones, una intervención está ligada a un objeto, por lo que
#es necesario que la clave primaria del objeto se ligue a un informe de estado. Por tanto
#como el hecho de que el usuario inserte una clave surrogada en la aplicación no es buena idea,
#se utilizan los datos iniciales de la variable datospre y en el fichero forms.py se hace que
#dicha casilla del formulario sea de sólo lectura.

@group_required('RestauradorBA')
def intervencion_crear(request, pk):
    datospre = get_object_or_404(InformeEstado, pk=pk)
    datadict = {'estado_rel': datospre.pk }
    if request.method == "POST":
      form = IntervencionForm(request.POST, initial=datadict)  
      if form.is_valid():
         instance = form.save()
         instance.user = request.user 
         instance.save()
         messages.success(request, 'Acción realizada con éxito')
         return HttpResponseRedirect('/')
       #si el formulario es valido se registra el objeto, que sera visible tanto desde el admin como desde
       #la interfaz en la vista de detalle
    else:
      form = IntervencionForm(initial=datadict)  
      return render(request, "Informes/formulario_intervencion.html",{"form": form,"datospre": datospre,})

@group_required('RestauradorARQ')
def informearqueo_crear(request,pk):
    instance = get_object_or_404(Objeto, pk=pk)
    datos =  Objeto.objects.filter().get(pk=instance.id)
    datadict = {'objeto': datos.id }
    if request.method == 'POST':
       form = InformeArqueoForm(request.POST, initial=datadict)
    #le pasamos el id del objeto mediante un diccionario inicial al formulario
    #de estado, de manera que el dato con el cual se relaciona la clase
    #informes estado no haya que rellenarlo    
       if form.is_valid():
         instance = form.save()
         instance.user = request.user 
         instance.save()
         messages.success(request, 'Acción realizada con éxito')
         return HttpResponseRedirect('/')
    else:
        form = InformeArqueoForm(initial=datadict)
       #si el formulario es valido se registra el objeto, que sera visible tanto desde el admin como desde
       #la interfaz en la vista de detalle
       #la interfaz en la vista de detalle
    return render(request, "formularios/formulario_informearqueo.html", {"form": form,"instance": instance,"datos": datos,})

@group_required('Documentador')
def movimiento_crear(request):
    if request.method == 'POST':
       form = MovimientoForm(request.POST)
       if form.is_valid():
         instance = form.save()
         instance.user = request.user 
         instance.save()
         messages.success(request, 'Acción realizada con éxito')
         return HttpResponseRedirect('/')
    else:
        form =MovimientoForm()
    return render(request, "formularios/formulario_movimiento.html", {"form": form,})   

'''

VISTAS DE ACTUALIZACIÓN DE OBJETOS YA EXISTENTES
EN LA BASE DE DATOS, ESTA TAREA SÓLO LA PUEDE REALIZAR EL DOCUMENTADOR
MENOS CON LOS INFORMES DE BELLAS ARTES Y DE ESTADO.

'''

#Si recibe una petición post el diccionario perteneciente al formulario de la vista
#estará ya poblado y se eviará un POST con los cambios realizados que guardará
#la instancia del objeto actualizado en la base de datos. En cambio si se recibe un GET
#se verán los datos anteriormente insertados para este objeto.

@group_required('Documentador')
def arqueologia_actualizar(request, pk):
    instance = get_object_or_404(Arqueologia, pk=pk)   
    if request.method == "POST":
      form = ArqueologiaForm(request.POST,request.FILES,instance=instance)
   
      if form.is_valid():
        instance = form.save()
        instance.save()
        messages.success(request, 'Acción realizada con éxito')
        return redirect('/') 
    else:
       form = ArqueologiaForm(instance=instance)    
       return render(request, "formularios/formulario_arqueologia.html", {'form':form,'instance':instance})
        

@group_required('Documentador')       
def bellasartes_actualizar(request, pk):
        instance = get_object_or_404(Bellasartes, pk=pk)
        if request.method == "POST":
           form = BellasArtesForm(request.POST,request.FILES, instance=instance)
           if form.is_valid():
            instance = form.save()
            instance.save()
            messages.success(request, 'Acción realizada con éxito')
            return HttpResponseRedirect(instance.get_absolute_url())
        else:
          form  = BellasArtesForm(instance=instance)   
        return render(request, "formularios/formulario_bellasartes.html", {"instance": instance, "form": form,})

@group_required('RestauradorBA')
def estado_actualizar(request, pk):
    instance = get_object_or_404(InformeEstado, pk=pk)
    if request.method == 'POST':
       form = InformeEstadoForm(request.POST, instance=instance)
       if form.is_valid():
         instance = form.save()
         instance.save()
         return HttpResponseRedirect(instance.get_absolute_url())
    else:
        form = InformeEstadoForm(instance=instance)
    return render(request, "Informes/formulario_estado.html", {"instance": instance,"form": form,})
 
   
@group_required('RestauradorARQ')
def informearqueo_actualizar(request, pk):
    instance = get_object_or_404(InformeArqueo, pk=pk)
    if request.method == 'POST':
      form = InformeArqueoForm(request.POST , instance=instance)
      if form.is_valid():
        instance = form.save()
        instance.save()
        messages.success(request, 'Acción realizada con éxito')
        return HttpResponseRedirect('/')
    else:
        form = InformeArqueoForm(instance=instance)  
    return render(request, "Informes/formulario_informearqueo.html", {"instance": instance,"form": form,})


'''

VISTAS VARIADAS, AQUÍ DEBERÍAN DE IR
LAS VISTAS AÑADIDAS EXTRAS DE INFORMACIÓN COMO PUEDE
SER LOS AUTORES CUYAS OBRAS ESTÁN EN COLECCIÓN EN EL MUSEO
Y LAS OBRAS ALMACENADAS DE CADA UNO.

'''
@group_required('Documentador')
def autor_actualizar(request, pk):
    instance = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
       form = AutorForm(request.POST, instance=instance)
       if form.is_valid():
          instance = form.save()
          instance.save()
          messages.success(request, 'Acción realizada con éxito')
          return HttpResponseRedirect('/')
    else:
         form = AutorForm(instance=instance)     
    return render(request, "formularios/formulario_autor.html", {"instance": instance,"form": form,})

@group_required('Documentador')
def iconografia_actualizar(request, pk):
    instance = get_object_or_404(Iconografia, pk=pk)
    if request.method == 'POST':
       form =IconografiaForm(request.POST, instance=instance)
       if form.is_valid():
        instance = form.save()
        instance.save()
        messages.success(request, 'Acción realizada con éxito')
        return HttpResponseRedirect('/')
    else:
        form = IconografiaForm(instance=instance)
    return render(request, "formularios/formulario_icon.html",{"instance": instance,"form": form,})

@group_required('Documentador')    
def soporte_actualizar(request, pk):
    instance = get_object_or_404(Soporte, pk=pk)
    if request.method == 'POST':
        form = SoporteForm(request.POST, instance=instance)
        if form.is_valid():
           instance = form.save()
           instance.save()
           messages.success(request, 'Acción realizada con éxito')
           return HttpResponseRedirect('/')
        else:
           messages.error(request, 'Corrija los fallos, por favor') 
    else:
        form = SoporteForm(instance=instance)
    return render(request, "formularios/formulario_sopo.html", {"instance": instance,"form": form,})

@group_required('Documentador')    
def edad_actualizar(request, pk):
    instance = get_object_or_404(Edad, pk)
    if request.method == 'POST':
        form =EdadForm(request.POST, instance=instance)
        if form.is_valid():
          instance = form.save()
          instance.save()
          messages.success(request, 'Acción realizada con éxito')
          return HttpResponseRedirect('/')
    else:
        form = EdadForm(instance=instance)
    return render(request, "formularios/formulario_edad.html",{"instance": instance,"form": form,})

@group_required('Documentador')
def tecnica_actualizar(request, pk):
    instance = get_object_or_404(Tecnica, pk=pk)
    if request.method == 'POST':
       form =TecnicaForm(request.POST,instance=instance)
       if form.is_valid():
         instance = form.save()
         instance.save()
         messages.success(request, 'Acción realizada con éxito')
         return HttpResponseRedirect('/')
    else:
        form = TecnicaForm(instance=instance)
    return render(request, "formularios/formulario_tecnica.html", {"instance": instance,"form": form,})
 
@group_required('Documentador')
def bibliografia_actualizar(request, pk):
    instance = get_object_or_404(Bibliografia, pk=pk)
    if request.method == 'POST':
        form = BibliografiaForm(request.POST,instance=instance)
        if form.is_valid():
          instance = form.save()
          instance.save()
          return HttpResponseRedirect('/')
    else:
        form = BibliografiaForm(instance=instance)
    return render(request, "formularios/formulario_biblio.html", {"instance": instance,"form": form,})

@group_required('Documentador')
def cultura_actualizar(request, pk):
    instance = get_object_or_404(Cultura, pk=pk)
    if request.method == 'POST':
        form = CulturaForm(request.POST, instance=instance)
        if form.is_valid():
          instance = form.save()
          instance.save()
          messages.success(request, 'Acción realizada con éxito')
          return HttpResponseRedirect('/')
    else:
        form = CulturaForm(instance=instance)  
    return render(request, "formularios/formulario_cultura.html",{"instance": instance,"form": form,})

@group_required('Documentador')
def yacimiento_actualizar(request, pk):
    instance = get_object_or_404(Yacimiento, pk=pk)
    if request.method == 'POST':
       form = YacimientoForm(request.POST,instance=instance)
       if form.is_valid():
         instance = form.save()
         instance.save()
         messages.success(request, 'Acción realizada con éxito')
         return HttpResponseRedirect('/')
    else:
        form = YacimientoForm(instance=instance)
    return render(request, "formularios/formulario_yacimiento.html", {"instance": instance,"form": form,})

def material_actualizar(request, pk):
    instance = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
       form = MaterialForm(request.POST,instance=instance)
       if form.is_valid():
         instance = form.save()
         instance.save()
         messages.success(request, 'Acción realizada con éxito')
         return HttpResponseRedirect('/')
    else:
        form = MaterialForm(instance=instance)
    return render(request, "formularios/formulario_material.html", {"instance": instance,"form": form,})



@group_required('Documentador')
def ubicacion_actualizar(request, pk):
    instance = get_object_or_404(Cultura, pk=pk)
    if request.method == 'POST':
        form = UbicacionForm(request.POST, instance=instance)
        if form.is_valid():
          instance = form.save()
          instance.save()
          messages.success(request, 'Acción realizada con éxito')
          return HttpResponseRedirect('/')
    else:
        form = UbicacionForm(instance=instance)  
    return render(request, "formularios/formulario_ubicacion.html",{"instance": instance,"form": form,})
'''

VISTAS DE BORRADO DE DATOS, TAREA
LA CUAL CON LOS OBJETOS DEL INVENTARIO DEL MUSEO
SÓLO PODRÁ REALIZAR EL DOCUMENTADOR. EN CAMBIO LOS RESTAURADORES PODRÁN
BORRAR SUS INFORMES.

'''

@group_required('Documentador')
def arqueologia_borrar(request, pk):
    instance = get_object_or_404(Arqueologia, pk=pk)
    instance.delete()
    messages.success(request, 'Acción realizada con éxito')
    return redirect("/verarqueologia")

@group_required('Documentador')
def bellasartes_borrar(request, pk):
    instance = get_object_or_404(Bellasartes, pk=pk)
    instance.delete()
    messages.success(request, 'Acción realizada con éxito')
    return redirect("/verbellasartes/")


'''

VISTAS DE DETALLE SOBRE OBJETOS E INFORMES,
AQUÍ SE VERÁ TODA LA INFORMACIÓN RELACIONADA CON
LOS OBJEOS INSERTADOS EN LA BASE DE DATOS.

'''

@login_required
def arqueologia_detalle(request, pk):
      instance = get_object_or_404(Arqueologia, pk=pk)
      estado = InformeArqueo.objects.filter(objeto=instance.pk)
      return render(request, "Listado/arqueologia_detail.html",{"titulo": instance.nombre, "instance":instance,"estado": estado})

@login_required
def bellasartes_detalle(request, pk):
      instance = get_object_or_404(Bellasartes, pk=pk)
      estado = InformeEstado.objects.filter(objeto=instance.id)
      return render(request, "Listado/bellasartes_detail.html", {"instance": instance, "estado": estado,})
      
@login_required
def estado_detalle(request, pk):
      instance = get_object_or_404(InformeEstado, pk=pk)
      datos = Bellasartes.objects.filter(pk=instance.objeto)
      datosobj = Objeto.objects.filter(pk=pk)
      # Guardar los datos de las consultas sobre el numero de inventario
      # que tiene el objeto que ha sido estudiado y/o intervenido
      #para no tener que volverlos a guardar en el formulario de estado
      intervencion = InformeIntervencion.objects.filter(estado_rel_id=instance.pk)
      #subconsulta arreglada, devolvía mas de un valor y por tanto no funcionaba
      # uso de context para guardar la informacion obtenida mediante las consultas anteriores para poder
      #rellenarlos
      return render(request, "Informes/estado_detail.html", {"instance": instance, "datos": datos,"datosobj": datosobj,"intervencion": intervencion,})

@login_required
def informearqueo_detalle(request, pk):
      instance = get_object_or_404(InformeArqueo, pk=pk)
      datos = Arqueologia.objects.filter(pk=instance.objeto)
      datosobj = Objeto.objects.filter(pk=pk)
    # Guardar los datos de las consultas sobre el numero de inventario
    # uso de context para guardar la informacion obtenida mediante las consultas anteriores para poder
    # utilizarlos en la plantilla
      return render(request, "Informes/informearqueo_detail.html",{"instance": instance, "datos" : datos,"datosobj": datosobj,})
    
      
'''

BÚSQUEDAS CON OBJETOS Q
Y CON FILTROS. BÚSQUEDA SIMPLE Y BÚSQUEDA
CON AND CON MÁS DE UNA COINCIDENCIA

'''      
@login_required
def arqueologia_lista(request):
    hoy = timezone.now().date()
    queryset_list = Arqueologia.objects.all() 
    if request.user.is_authenticated():
      queryset_list = Arqueologia.objects.all()
      query = request.GET.get("q")
      if query:
        queryset_list = queryset_list.filter(
            Q(nombre__icontains=query)|
            Q(numinv__icontains=query)
            ).distinct()
    paginator = Paginator(queryset_list, 10) 
    page_request_var = "list"
    page = request.GET.get(page_request_var)
    try:
       queryset = paginator.page(page)
    except PageNotAnInteger:
      queryset = paginator.page(1)
    except EmptyPage:
      queryset = paginator.page(paginator.num_pages)
    return render(request, "Listado/arqueologia_lista.html", {"nombre": "List","object_list": queryset,"page_request_var": page_request_var,"hoy": hoy,})

@login_required
def bellasartes_lista(request):
    hoy = timezone.now().date()
    queryset_list = Bellasartes.objects.all()
    if request.user.is_authenticated():
      query = request.GET.get("q")
      if query:
        queryset_list = queryset_list.filter(
            Q(titulo__icontains=query)|
            Q(numinv__icontains=query)|
            Q(autor__nombre__icontains=(query))|
            Q(autor__alias__icontains=(query))|
            Q(autor__apellidos__icontains=(query))
            ).distinct()
    paginator = Paginator(queryset_list, 3)
    page_request_var = "list"
    page = request.GET.get(page_request_var)
    try:
       queryset = paginator.page(page)
    except PageNotAnInteger:
    
      queryset = paginator.page(1)
    except EmptyPage:     
      queryset = paginator.page(paginator.num_pages)   
    return render(request, "Listado/bellasartes_lista.html", {"object_list": queryset,"page_request_var": page_request_var, "hoy": hoy, })


#BUSQUEDAS DE ARQUEOLOGIA A PARTIR DE UNA VISTA DE LISTADO
@login_required
def searcharqueologia(request):
    arqueologia_list = Arqueologia.objects.all()
    arqueologia_filter = ArqueologiaFilter(request.GET, queryset=arqueologia_list)
    return render(request, 'Busqueda/arqueologia_search.html', {'filter': arqueologia_filter})
    
#BUSQUEDA DE BELLAS ARTES A PARTIR DE UNA VISTA DE LISTADO
@login_required
def searchbellasartes(request):
    bellasartes_list = Bellasartes.objects.all()
    bellasartes_filter = BellasArtesFilter(request.GET, queryset=bellasartes_list)
    return render(request, 'Busqueda/bellasartes_search.html', {'filter': bellasartes_filter})


#funcion del pop up para los objetos con foreign key en otros modelos
#recibe una peticion,un formulario y un campo que sera
#el que vayamos a agregar
@login_required
def handlePopAdd(request, addForm, field):
   form = addForm()
   if request.method == "POST" or request.method == "GET":
       form = addForm(request.POST)            
       if form.is_valid():
            newObject = form.save()
       else:
            newObject = None
       if newObject:
           return HttpResponse('<h2>Agregado con éxito, cierre la página</h2>')
       else:
            form = addForm()
            pageContext = {'form': form, 'field': field}
       return render(request,"widget/popadd.html", pageContext)

# Errores con plantilla personalizada para utilizar en producción

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
    
#CREACION DE DATOS LOOK-UP
@login_required
def newBibliografia(request):
    return handlePopAdd(request, BibliografiaForm, 'Bibliografia')
    
@login_required   
def newUbicacion(request):
	return  handlePopAdd(request, UbicacionForm, 'Ubicacion')
    
@login_required
def newMovimiento(request):
	return  handlePopAdd(request, MovimientoForm, 'Movimiento')
    
@login_required
def newEstudio(request):
    return handlePopAdd(request, EstudioForm, 'Estudio')

#vistas de los formularios de adicion de objetos de arqueologia
@login_required
def newMaterial(request):
     return handlePopAdd(request, MaterialForm, 'Material')
@login_required
def newSeccion(request):
    return handlePopAdd(request, SeccionForm, 'Seccion')
@login_required
def newYacimiento(request):
    return handlePopAdd(request, YacimientoForm, 'Yacimiento')
@login_required
def newSerie(request):
    return handlePopAdd(request, SerieForm, 'Serie')
@login_required
def newCultura(request):
    return handlePopAdd(request, CulturaForm, 'Cultura')

#vistas de los formularios de adicion de informacion de objetos de bellas artes
@group_required('Documentador')
def newAutor(request):
     return handlePopAdd(request, AutorForm, 'Autor')

@group_required('Documentador')
def newTecnica(request):
    return handlePopAdd(request, TecnicaForm, 'Tecnica')

@group_required('Documentador')
def newSoporte(request):
    return handlePopAdd(request, SoporteForm, 'Soporte')

@group_required('Documentador')
def newPais(request):
    return handlePopAdd(request, PaisForm, 'Soporte')
    
@group_required('Documentador')
def newDonante(request):
    return handlePopAdd(request, DonanteForm, 'Donante')

@group_required('Documentador')
def newEstilo(request):
    return handlePopAdd(request, EstiloForm, 'Estilo')

@group_required('Documentador')
def newIconografia(request):
    return handlePopAdd(request, IconografiaForm, 'Iconografia')
    
@group_required('Documentador')
def newEscritor(request):
    return handlePopAdd(request, EscritorForm, 'Escritor')
    
#Vista que devuelve los autores de bellas artes
#los cuales tienen obras pertenecientes a ellos en el
#museo, se presenta una foto y una pequeña biografía

@login_required
def autores_lista(request):
    queryset_list = Autor.objects.all()
    if request.user.is_authenticated():
      query = request.GET.get("q")
      if query:
        queryset_list = queryset_list.filter(
            Q(nombre__icontains=query)|
            Q(apellidos__icontains=(query))
            ).distinct()
    paginator = Paginator(queryset_list, 2)
    page_request_var = "list"
    page = request.GET.get(page_request_var)
    try:
       queryset = paginator.page(page)
    except PageNotAnInteger:
      queryset = paginator.page(1)
    except EmptyPage:
      queryset = paginator.page(paginator.num_pages)
    return render(request, "Listado/autores_lista.html", {"object_list": queryset,"page_request_var": page_request_var,})

    
#vista que une a cada autor con sus obras y una pequeña referencia, tambien
#puede ser util para ver colecciones, por ejemplo, algún dia puede ser
#útil consultar la coleccion de "Alberti"

@login_required
def autores_clasi(request,pk):
    instance = get_object_or_404(Autor, pk=pk)
    cuadros = Bellasartes.objects.filter(autor=instance).values()
    return render(request, "Listado/autores_clasi.html",{"instance": instance, "cuadros": cuadros,})



