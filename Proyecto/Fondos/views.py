#!/usr/bin/env python
# -*- coding: utf-8 -*
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from .models import *
from .forms import *
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.utils.html import escape
from django.core.urlresolvers import reverse
from django.shortcuts import render
from .filters import ArqueologiaFilter,BellasArtesFilter
from django.contrib.admin import widgets   
from django.conf import settings
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.conf import settings
from django.views.generic import View
from django import http
from django.template.loader import get_template
from django.template import Template, RequestContext
from django.template import Context
from django.contrib import auth
from django.contrib.auth.models import User
from django.forms import formset_factory



def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Contraseña correcta y usuario activo
        auth.login(request, user)
        # Redireccion a una pagina de exito
        return HttpResponseRedirect("/account/loggedin/")
    else:
        # Muestra pagina de error
        return HttpResponseRedirect("/account/invalid/")

@login_required
def index(request):
    #Dependiendo del rol de cada usuario, verá algo distinto en el inicio de la página
    #en cambio, si es usuario administrador o staff será redirigido a su interfaz de admin
   if request.user.is_authenticated() and request.user.is_superuser==False :
      group_name = request.user.groups.all()[0].name
      if group_name == "Documentador":
        ultimosarqueo = Arqueologia.objects.all().order_by('-fechaingreso')[:10]
        ultimosba = Bellasartes.objects.all().order_by('-fechaingreso')[:10]
        context = { "ultimosarqueo":ultimosarqueo,
                    "ultimosba":ultimosba }
        return render(request, "homedocu.html",context)
      if group_name == "RestauradorBA":
          ultimosinfo = InformeEstado.objects.all().order_by('-fecha')[:3]
          context = { "ultimosinfo":ultimosinfo }
          return render(request, "homerestauba.html",context)
      if group_name == "RestauradorARQ":
          ultimosinfo = InformeArqueo.objects.all().order_by('-fecha')[:3]
          context = { "ultimosinfo":ultimosinfo }
          return render(request, "homerestauar.html",context)
   else:
        return HttpResponseRedirect('/admin/')
  
#PARTE DE LOLA Y JOSE CARLOS
def arqueologia_crear(request): 
    #~ group_name = request.user.groups.all()[0].name
    #~ if group_name != "Documentador":
       #~ return PermissionDenied
    form = ArqueologiaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user 
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form
    }
    return render(request, "formularios/formulario_arqueologia.html", context)

# editar objeto de arqueologia existente
def arqueologia_actualizar(request, pk=None):
    instance = get_object_or_404(Arqueologia, pk=pk)
    form = ArqueologiaForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
      instance = form.save(commit=False)
      instance.save()
      return HttpResponseRedirect(instance.get_absolute_url())
    context = {
         "instance": instance,
         "form": form,
     }
    return render(request, "formularios/formulario_arqueologia.html", context)

#detalle de arqueologia
def arqueologia_detalle(request, pk=None):
      instance = get_object_or_404(Arqueologia, pk=pk)
      estado = InformeArqueo.objects.filter(objeto=instance.pk)
      context = {
      "titulo": instance.nombre,
      "instance": instance,
      "estado": estado
}
      return render(request, "Listado/arqueologia_detail.html", context)
      
def arqueologia_borrar(request, pk=None):
    instance = get_object_or_404(Arqueologia, pk=pk)
    instance.delete()
    return redirect("/inicio/verarqueologia")

# Vista listado y busqueda simple

@login_required
def arqueologia_lista(request):
    hoy = timezone.now().date()
    queryset_list = Arqueologia.objects.all() #filter(draft=False).filter(publish__lte=timezone.now()) #all() #.order_by("-timestamp")
    if request.user.is_authenticated():
      queryset_list = Arqueologia.objects.all()
      query = request.GET.get("q")
      if query:
        queryset_list = queryset_list.filter(
            Q(nombre__icontains=query)|
            Q(numinv__icontains=query)
            ).distinct()
    paginator = Paginator(queryset_list, 3) # Show 25 contacts per page
    page_request_var = "list"
    page = request.GET.get(page_request_var)
    try:
       queryset = paginator.page(page)
    except PageNotAnInteger:
      # If page is not an integer, deliver first page.
      queryset = paginator.page(1)
    except EmptyPage:
      # If page is out of range (e.g. 9999), deliver last page of results.
      queryset = paginator.page(paginator.num_pages)
    context = {
     "nombre": "List",
     "object_list": queryset,
     "page_request_var": page_request_var,
     "hoy": hoy,
   }
    return render(request, "Listado/arqueologia_lista.html", context)

#funcion del pop up para los objetos con foreign key en otros modelos
#recibe una peticion,un formulario y un campo que sera
#el que vayamos a agregar

def handlePopAdd(request, addForm, field):
   form = addForm()
   if request.method == "POST" or request.method == "GET":
       form = addForm(request.POST)            
       if form.is_valid():
            newObject = form.save()
       else:
            newObject = None
       if newObject:
           return HttpResponse('<script type="text/javascript">opener.dismissAddAnotherPopup(window, "%s", "%s");</script>' % \
            (escape(newObject._get_pk_val()), escape(newObject)))
       else:
            form = addForm()
            pageContext = {'form': form, 'field': field}
       return render(request,"widget/popadd.html", pageContext)


# Errores con plantilla personalizada

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
    
def newBibliografia(request):
    return handlePopAdd(request, BibliografiaForm, 'Bibliografia')
    
def newUbicacion(request):
	return  handlePopAdd(request, UbicacionForm, 'Ubicacion')

def newMovimiento(request):
	return  handlePopAdd(request, MovimientoForm, 'Movimiento')

#~ def newInformeEstado(request):
	#~ return  handlePopAdd(request, InformeEstadoForm, 'InformeEstado')

#
#   VISTAS DE BELLAS ARTES
#

def bellasartes_crear(request):
    form = BellasArtesForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user 
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form
    }
    return render(request,'formularios/formulario_bellasartes.html', {'form': form})


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
      
    context = {
     "object_list": queryset,
     "page_request_var": page_request_var,
     "hoy": hoy,
   }
    return render(request, "Listado/bellasartes_lista.html", context)
    

def bellasartes_actualizar(request, pk=None):
    instance = get_object_or_404(Bellasartes, pk=pk)
    form = BellasArtesForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
      instance = form.save(commit=False)
      instance.save()
      return HttpResponseRedirect(instance.get_absolute_url())
    context = {
         "nombre": instance.titulo,
         "instance": instance,
         "form": form,
     }
    return render(request, "formularios/formulario_bellasartes.html", context)

def bellasartes_detalle(request, pk=None):
      instance = get_object_or_404(Bellasartes, pk=pk)
      estado = InformeEstado.objects.filter(objeto=instance.id)
      
      if not request.user.is_authenticated():
         raise Http404
      context = {
      "instance": instance,
      "estado": estado,
}
      return render(request, "Listado/bellasartes_detail.html", context)

def bellasartes_borrar(request, pk=None):
    if not request.user.is_authenticated() and not request.user.is_documentador():
      raise Http404
    instance = get_object_or_404(Bellasartes, pk=pk)
    instance.delete()
    messages.success(request, "Se ha eliminado el objeto.")
    return redirect("/inicio/verbellasartes/")

def newEstudio(request):
    return handlePopAdd(request, EstudioForm, 'Estudio')

#vistas de los formularios de adicion de objetos de arqueologia


def newMaterial(request):
     return handlePopAdd(request, MaterialForm, 'Material')

def newSeccion(request):
    return handlePopAdd(request, SeccionForm, 'Seccion')


def newYacimiento(request):
    return handlePopAdd(request, YacimientoForm, 'Yacimiento')

def newSerie(request):
    return handlePopAdd(request, SerieForm, 'Serie')

def newCultura(request):
    return handlePopAdd(request, CulturaForm, 'Cultura')

#vistas de los formularios de adicion de informacion de objetos de bellas artes

def newAutor(request):
     return handlePopAdd(request, AutorForm, 'Autor')

def newTecnica(request):
    return handlePopAdd(request, TecnicaForm, 'Tecnica')

def newSoporte(request):
    return handlePopAdd(request, SoporteForm, 'Soporte')

def newDonante(request):
    return handlePopAdd(request, DonanteForm, 'Donante')
    
def newEstudio(request):
    return handlePopAdd(request, EstudioForm, 'Estudio')
    
def newMovimiento(request):
    return handlePopAdd(request, MovimientoForm, 'Movimiento')
    
def newEstilo(request):
    return handlePopAdd(request, EstiloForm, 'Estilo')

def newIconografia(request):
    return handlePopAdd(request, IconografiaForm, 'Iconografia')
#BUSQUEDAS DE ARQUEOLOGIA A PARTIR DE UNA VISTA DE LISTADO

#busqueda avanzada mediante la aplicación django-filter

@login_required
def searcharqueologia(request):
    arqueologia_list = Arqueologia.objects.all()
    arqueologia_filter = ArqueologiaFilter(request.GET, queryset=arqueologia_list)
    return render(request, 'Busqueda/arqueologia_search.html', {'filter': arqueologia_filter})
    
    
#BUSQUEDA DE BELLAS ARTES A PARTIR DE UNA VISTA DE LISTADO

def searchbellasartes(request):
    bellasartes_list = Bellasartes.objects.all()
    bellasartes_filter = BellasArtesFilter(request.GET, queryset=bellasartes_list)
    return render(request, 'Busqueda/bellasartes_search.html', {'filter': bellasartes_filter})    

#VISTAS DE ESTADOS E INTERVENCIONES 

#PARTE DE MARISA
def estado_crear(request, pk=None):
    instance = get_object_or_404(Objeto, pk=pk)
    datos =  Objeto.objects.filter().get(pk=instance.id)
    datadict = {'objeto': datos.pk }
    form = InformeEstadoForm(request.POST or None, initial=datadict)    
    #le pasamos el id del objeto mediante un diccionario inicial al formulario
    #de estado, de manera que el dato con el cual se relaciona la clase
    #informes estado no haya que rellenarlo    
    if form.is_valid():
       instance = form.save(commit=False)
       instance.user = request.user 
       instance.save()
       form.save_m2m()
       messages.success(request, "Se ha registrado el objeto") #esto se ve en el admin
       return HttpResponseRedirect('/') 
       #si el formulario es valido se registra el objeto, que sera visible tanto desde el admin como desde
       #la interfaz en la vista de detalle
    context = {
         "form": form,
         "instance": instance,
         "datos": datos
    }
    return render(request, "Informes/formulario_estado.html", context)


def estado_detalle(request, pk=None):
      instance = get_object_or_404(InformeEstado, pk=pk)
      datos = Bellasartes.objects.filter(pk=instance.objeto)
      datosobj = Objeto.objects.filter(pk=pk)
      # Guardar los datos de las consultas sobre el numero de inventario
      # que tiene el objeto que ha sido estudiado y/o intervenido
      #para no tener que volverlos a guardar en el formulario de estado
      intervencion = InformeIntervencion.objects.filter(estado_rel_id=instance.pk)
      #subconsulta arreglada, devolvía mas de un valor y por tanto no funcionaba
    # uso de context para guardar la informacion obtenida mediante las consultas anteriores para poder
    # utilizarlos en la plantilla
      context = {
      "instance": instance,
      "datos": datos,
      "datosobj": datosobj,
      "intervencion": intervencion,
}
      return render(request, "Informes/estado_detail.html", context)
      
#Actualizar un informe de estado   
def estado_actualizar(request, pk=None):
    instance = get_object_or_404(InformeEstado, pk=pk)
    form = InformeEstadoForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
      instance = form.save(commit=False)
      instance.save()
      return HttpResponseRedirect(instance.get_absolute_url())
    context = {
         "instance": instance,
         "form": form,
     }
    return render(request, "Informes/formulario_estado.html", context)
    
 
def intervencion_crear(request, pk=None):
    if not request.user.is_authenticated():
       raise Http404
    datospre = get_object_or_404(InformeEstado, pk=pk)
    datadict = {'estado_rel': datospre.pk }
    form = IntervencionForm(request.POST or None, initial=datadict)
    
    if form.is_valid():
       instance = form.save(commit=False)
       instance.user = request.user 
       instance.save()
       messages.success(request, "Se ha registrado el objeto") #esto se ve en el admin
       return HttpResponseRedirect('/')
       
       #si el formulario es valido se registra el objeto, que sera visible tanto desde el admin como desde
       #la interfaz en la vista de detalle
    context = {
         "form": form,
         "datospre": datospre,
    }
    return render(request, "Informes/formulario_intervencion.html", context)
    

# PARTE DE LUIS CARLOS
# Informes de arqueologia
def informearqueo_crear(request,pk):
    instance = get_object_or_404(Objeto, pk=pk)
    datos =  Objeto.objects.filter().get(pk=instance.id)
    datadict = {'objeto': datos.id }
    form = InformeArqueoForm(request.POST or None, initial=datadict)
    #le pasamos el id del objeto mediante un diccionario inicial al formulario
    #de estado, de manera que el dato con el cual se relaciona la clase
    #informes estado no haya que rellenarlo    
    if form.is_valid():
       instance = form.save()
       instance.user = request.user 
       instance.save()
       messages.success(request, "Se ha registrado el objeto") #esto se ve en el admin
       return HttpResponseRedirect('/')
       #si el formulario es valido se registra el objeto, que sera visible tanto desde el admin como desde
       #la interfaz en la vista de detalle
              #la interfaz en la vista de detalle
    context = {
         "form": form,
         "instance": instance,
         "datos": datos,
    }
    
    return render(request, "formularios/formulario_informearqueo.html", context)

def informearqueo_detalle(request, pk=None):
      instance = get_object_or_404(InformeArqueo, pk=pk)
      datos = Arqueologia.objects.filter(pk=instance.objeto)
      datosobj = Objeto.objects.filter(pk=pk)
    # Guardar los datos de las consultas sobre el numero de inventario
    # uso de context para guardar la informacion obtenida mediante las consultas anteriores para poder
    # utilizarlos en la plantilla
      context = {
      "instance": instance,
      "datos" : datos,
      "datosobj": datosobj,
}
      return render(request, "Informes/informearqueo_detail.html", context)
      
#Actualizar un informe de estado   
def informearqueo_actualizar(request, pk=None):
    instance = get_object_or_404(InformeArqueo, pk=pk)
    form = InformeArqueoForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
      instance = form.save()
      instance.save()
      return HttpResponseRedirect('/')
    context = {
         "instance": instance,
         "form": form,
     }
    return render(request, "Informes/formulario_informearqueo.html", context)

        
#Vista que devuelve los autores de bellas artes
#los cuales tienen obras pertenecientes a ellos en el
#museo, se presenta una foto y una pequeña biografía

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
    context = {
    "object_list": queryset,
    "page_request_var": page_request_var,

   }
    return render(request, "Listado/autores_lista.html", context)

    
#vista que une a cada autor con sus obras y una pequeña referencia, tambien
#puede ser util para ver colecciones, por ejemplo, algún dia puede ser
#útil consultar la coleccion de "Alberti"

def autores_clasi(request,pk):
    instance = get_object_or_404(Autor, pk=pk)
    cuadros = Bellasartes.objects.filter(autor=instance).values()
    context = {
     "instance": instance,
     "cuadros": cuadros,
   }
    return render(request, "Listado/autores_clasi.html", context)


