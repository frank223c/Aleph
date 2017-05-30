#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url,include
from .views import *
from django.contrib.auth import views
from .forms import LoginForm
from .forms import *

urlpatterns = [
    url(r'^$',index, name='index'),
    url(r'^accounts/login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^inicio/logout/$', views.logout, {'next_page': 'login'}), 
    #VISTA DEL SUPER FORMULARIO DE ARQUEOLOGIA
    url(r'^registrararqueologia', arqueologia_crear , name='registrararqueologia'),
    url(r'^registrarbellasartes', bellasartes_crear , name='registrarbellasartes'),
    url(r'^verarqueologia', arqueologia_lista , name='verarqueologia'),
    url(r'^verbellasartes', bellasartes_lista , name='verbellasartes'),
    url(r'^arqueologia/(?P<pk>\d+)/$', arqueologia_detalle, name='detallearqueo'),
    url(r'^bellasartes/(?P<pk>\d+)/$', bellasartes_detalle, name='detallebellasartes'),
    #url(r'^autores/(?P<pk>\d+)/$', autor_detalle, name='detallebeautores'),
    url(r'^arqueologia/(?P<pk>\d+)/editar/$', arqueologia_actualizar, name='actualizararqueologia'),
    url(r'^bellasartes/(?P<pk>\d+)/editar/$', bellasartes_actualizar, name='actualizarbellasartes'),
    url(r'^arqueologia/(?P<pk>\d+)/borrar/$', arqueologia_borrar, name='borrararqueologia'),
    url(r'^bellasartes/(?P<pk>\d+)/borrar/$', bellasartes_borrar, name='borrarbellasartes'),
    #VISTAS PARA AGREGAR ELEMENTOS EXTERNOS DE LA TABLA OBJETO
    url(r'^agregar/bibliografia/',newBibliografia, name='nuevabibliografia'),
    url(r'^agregar/ubicacion/',newUbicacion, name='nuevaubicacion'),
    url(r'agregar/movimientos/', newMovimiento, name='nuevo-movimiento'),
    url(r'^agregar/estudio/' ,newEstudio, name='nuevoestudio'),
    #VISTAS PARA AGREGAR ELEMENTOS DE TABLAS EXTERNAS DE ARQUEOLOGIA
    url(r'^agregar/material/',newMaterial, name='nuevomaterial'),
    url(r'^agregar/cultura/',newCultura, name='nuevacultura'),
    url(r'^agregar/seccion/',newSeccion, name='nuevaseccion'),
    url(r'^agregar/serie/',newSerie, name='nuevaserie'),
    url(r'^agregar/yacimiento/',newYacimiento, name='nuevoyacimiento'),
    #VISTAS PARA AGREGAR ELEMENTOS EXTERNOS DE BA
    url(r'^agregar/donante/',newDonante, name='nuevodonante'),
    url(r'^agregar/tecnica/',newTecnica, name='nuevotecnica2'),
    url(r'^agregar/soporte/',newSoporte, name='nuevosoporte'),
    url(r'^agregar/Soporte/',newSoporte, name='nuevosoporte2'),
    url(r'^agregar/autor/',newAutor, name='nuevoautor2'),
    url(r'^agregar/iconografia/',newIconografia, name='nuevoiconografia'),
    #BUSQUEDAS
    url(r'^search-arqueologia/$',searcharqueologia, name='search-arqueologia'),
    url(r'^search-bellasartes/$',searchbellasartes, name='search-bellasartes'),
    #LISTADO
    url(r'^registrarestado/(?P<pk>\d+)/$', estado_crear , name='registrarestado'),
    url(r'^registrarintervencion/(?P<pk>\d+)/$', intervencion_crear , name='registrarintervencion'),
    #url(r'^registrarintervencion', intervencion_crear , name='registrarintervencion'),
    url(r'^estado/(?P<pk>\d+)/$', estado_detalle, name='detalleestado'),
    url(r'^estadoactualizar/(?P<pk>\d+)/$', estado_actualizar, name='actuestado'),
    url(r'^autor_clasificacion/(?P<pk>\d+)/$', autores_clasi, name='autores-clasificacion'),
    url(r'^verautores', autores_lista, name='autores-listado'),
    #url(r'^generainforme', get_reporte, name='informe'),

]



handler404 = handler404
handler500 = handler500
