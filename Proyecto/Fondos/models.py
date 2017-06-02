#!/usr/bin/env python
# -*- coding: utf-8 -*
from __future__ import unicode_literals
from django.db import models
from django.core.files import File
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db.models import Max,Avg
from django.conf import settings 
import os.path
from uuid import uuid4
from django.utils.encoding import smart_text, smart_unicode,smart_str

smart_text(str)
smart_str(str)
smart_unicode(str)


def path_and_rename(instance, filename):
    upload_to = 'Miniaturas'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}_{}.{}'.format(instance.codigo,instance.numinv, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)
    

class Bibliografia(models.Model):
    autor = models.CharField(max_length=20)
    titulo = models.CharField(max_length=60)
    anio = models.CharField(max_length=30,verbose_name="Año la publicacion")
    pagina = models.CharField(max_length=30,verbose_name="Página")
    edicion = models.CharField(max_length=10,verbose_name="Edicion")
    extracto = models.TextField(blank=True)  
    isbn = models.CharField(max_length=13, blank=True,verbose_name="ISBN")
    url = models.URLField(max_length=500, blank=True,default='') #referencias externas

    def __str__(self):
      return str(self.titulo) + str(self.anio)

    class Meta:
        ordering = ["edicion"]
        verbose_name_plural = "Bibliografias"

class Movimiento(models.Model): 
    ciudad = models.CharField(max_length=20,verbose_name="Ciudad")
    museo = models.CharField(max_length=30,verbose_name="Museo")
    nombre_exposicion = models.CharField(max_length=30,verbose_name="Exposicion")
    fecha_prestado = models.DateField(auto_now=False)
    fecha_devuelto = models.DateField(auto_now=False)
    
    def __str__(self):
      return str(self.fecha_prestado) + " "  + str(self.fecha_devuelto) + " " + str(self.ciudad) +   " " + str(self.museo) + " " +  str(self.nombre_exposicion) 
    class Meta:
        ordering = ["fecha_prestado"]
        verbose_name_plural = "Movimientos"

class Estudio(models.Model):
    nombre = models.CharField(max_length=20)
    def __str__(self):
        return str(self.nombre)

        
class Objeto(models.Model):
    anverso = models.ImageField(upload_to=path_and_rename)
    reverso  = models.ImageField(upload_to=path_and_rename)
    codigo_selec = (('DJ', 'DJ'),
               ('CE', 'CE'),
               ('DO', 'DO'),
               ('DE', 'DE'),
               )
    codigo = models.CharField(choices = codigo_selec, max_length=2,default='DJ',verbose_name="Código") 
    numinv = models.IntegerField(unique=True,default=1,verbose_name="Número de inventario")  # Field name made lowercase.
    altura = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Altura en cm") 
    ancho = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Ancho en cm") 
    datacion = models.CharField(max_length=30,default='Desconocida',verbose_name="Fecha de la que data el objeto")
    bibliografia = models.ManyToManyField(Bibliografia,blank=True)
    fechaingreso = models.CharField(max_length=30,verbose_name="Fecha de ingreso")
    ubicacionmus = models.CharField(max_length=30,verbose_name="Ubicacion en el museo")
    movimientos = models.ManyToManyField(Movimiento,blank=True,null=True) #histórico de prestamos a otros museos para exposiciones
    descripcion = models.TextField() 
    observaciones = models.TextField() 

    def __str__(self):
      return str(self.id)

#Campos especificos de arqueologia

class Serie(models.Model):
    nombre =  models.CharField(max_length=40)

    def __str__(self):
	    return str(self.nombre)
    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Series"


class Material(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
	    return str(self.nombre)
    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Materiales"
            
class Seccion (models.Model):
    nombre = models.CharField(max_length=10)
   
    def __str__(self):
	    return str(self.nombre)
    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Secciones de arqueologia"

class Cultura(models.Model):
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
	    return str(self.nombre)
    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Culturas"
        

#Fondos.Arqueologia.numinv: (fields.W342) Setting unique=True on a ForeignKey has the same effect as using a OneToOneField.
#       HINT: ForeignKey(unique=True) is usually better served by a OneToOneField.
#Fondos.Bellasartes.numinv: (fields.W342) Setting unique=True on a ForeignKey has the same effect as using a OneToOneField.
#        HINT: ForeignKey(unique=True) is usually better served by a OneToOneField.

class Yacimiento(models.Model):
    yacimiento = models.CharField(max_length=30)  
    municipio =  models.CharField(max_length=30)
    localidad =  models.CharField(max_length=30)
   
    def __str__(self):
	    return str(self.yacimiento) + " , " +  str(self.municipio)
    class Meta:
        ordering = ["yacimiento"]
        verbose_name_plural = "Yacimientos de arqueologia"

class Arqueologia(Objeto):
    nombre = models.CharField(max_length=30)
    seccion = models.ForeignKey(Seccion,null=True)
    hallazgos = models.TextField(blank=True, null=True)
    depositado =  models.CharField(max_length=20,null=False)
    cultura = models.ForeignKey(Cultura)
    serie = models.ForeignKey(Serie)
    conservacion_selec = (('1', 'Bueno'),
               ('2', 'Regular'),
               ('3', 'Malo'),
               )
    conservacion = models.CharField(choices = conservacion_selec,max_length=1,default='1') 
    yacimiento = models.ForeignKey(Yacimiento)
    edad_selec = (('Edad de piedra', 'Edad de piedra'),
               ('Edad de bronce', 'Edad de bronce'),
               ('Edad de metal', 'Edad de metal'),
               ('Edad de hierro', 'Edad de hierro'),
               ('Edad moderna', 'Edad moderna'),
               ('Edad de piedra', 'Edad desconocida'),
               )
    edad = models.CharField(choices = edad_selec,
                            default='Edad desconocida',max_length=17) 
    material = models.ManyToManyField(Material)
   
    def __str__(self):
       return " Nombre:" + str(self.nombre) + " Sección:" + str(self.seccion) + " Edad:" + str(self.edad) + " Cultura:" + str(self.cultura)

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Arqueologia"
    def get_absolute_url(self):
        return "/arqueologia/%i/" % self.pk


# Aqui termina la parte de arqueologia
# Comienza los modelos
# de bellas Artes con sus campos especificos

class Tecnica(models.Model):
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
	       return str(self.nombre) 
    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Tipos de tecnicas"

class Soporte(models.Model):
    nombre = models.CharField(max_length=10)
 
    def __str__(self):
      return str(self.nombre)
    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Tipos de soportes"


class Donante(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    dni = models.CharField(max_length=9,blank=True)
    
    def __str__(self):
	    return str(self.nombre) +  " " + str(self.apellidos) 
    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Donantes"
        
class Iconografia(models.Model):
    nombre = models.CharField(max_length=30,verbose_name="Iconografia")
    descripcion = models.TextField(blank=True)
    
    def __str__(self):
	    return str(self.nombre) 
    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Iconografias"

class Autor(models.Model):
    foto = models.ImageField(upload_to='autores',default='nofoto.png')
    alias = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=40,default='Desconocida')
    procedencia = models.CharField(max_length=40,default='Desconocida')
    fnac = models.CharField(max_length=14,default='Desconocida')
    fdef = models.CharField(max_length=14,default='Desconocida')
    refbiografia = models.URLField(max_length=50, blank=True)

    def __str__(self):
	      return str(self.nombre) + " ," + str(self.alias)
    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Autores"
     
     
class Bellasartes(Objeto):
    titulo = models.CharField(max_length=40)
    iconografia = models.ForeignKey(Iconografia,blank=True)
    procedencia = models.CharField(max_length=20)
    soporte = models.ManyToManyField(Soporte)
    tecnica = models.ManyToManyField(Tecnica,blank=True)
    adquirido_selec = (('Compra', 'Compra'),
               ('Donacion', 'Donacion'),
               ('Legado', 'Legado'),
               )
    autor = models.ForeignKey(Autor,blank=True)
    formaingreso = models.CharField(choices = adquirido_selec,max_length=8,default='1',verbose_name="Forma de ingreso") 
    donante = models.ForeignKey(Donante,blank=True,null=True)
    def __str__(self):
	       return str(self.titulo) +  " " + str(self.autor)
    class Meta:
        ordering = ["titulo"]
        verbose_name_plural = "Bellas Artes"
    def get_absolute_url(self):
        return "/bellasartes/%i/" % self.pk


class InformeEstado(models.Model):
    objeto = models.ForeignKey(Objeto, verbose_name="Objeto sobre el que se realiza el informe") #id del objeto 
    nombre_res = models.CharField(max_length=30,verbose_name=("Nombre restaurador"))
    ape_res = models.CharField(max_length=50,verbose_name=("Apellidos del restaurador"))
    objeto = models.ForeignKey(Objeto, verbose_name="Objeto sobre el que se realiza el informe") #id del objeto 
    fecha = models.DateField(auto_now=True,verbose_name=("Fecha del informe de estado")) #fecha cuando se realiza el informe
    cartela = models.TextField() 
    marco = models.TextField(blank=True)
    montaje = models.TextField(blank=True)
    estudio = models.ManyToManyField(Estudio, verbose_name="Estudios realizados")
    muestras = models.BooleanField(default=False) #se han tomado muestras o no
    obra = models.TextField(blank=True)
    conclusion = models.TextField()
    prioridad = models.IntegerField(verbose_name="Prioridad",validators=[MinValueValidator(1),MaxValueValidator(6)]) #de menos a más
    propuesta = models.TextField()
    metodologia = models.TextField()
    
    def __str__(self):
       return  " Prioridad:" + str(self.prioridad)
           
    class Meta:
        ordering = ["fecha"]
        verbose_name_plural = "Estados" 
   
    def get_absolute_url(self):
        return "/verbellasartes/"

      
class InformeIntervencion(models.Model):
    estado_rel = models.OneToOneField(InformeEstado, primary_key=True)
    tipo = models.CharField(max_length=80)
    justificacion = models.TextField(verbose_name="Justificación de la intervencion")
    criterios = models.TextField()
    estudios = models.BooleanField(default=False)
    fecha =  models.DateField(auto_now=True,verbose_name=("Fecha del informe de estado"))
    priori_des = models.IntegerField(verbose_name="Prioridad tras intervencion",validators=[MinValueValidator(1),MaxValueValidator(6)])
    descripcioninter = models.TextField(verbose_name="Descripcion")
    recom = models.TextField(verbose_name="Recomendaciones")
    
    def __str__(self):
        return str(self.estado_rel) + str(self.priori_des)
    class Meta:
        ordering = ["fecha"]
        verbose_name_plural = "Intervenciones"

      
class InformeArqueo(models.Model):
    objeto = models.ForeignKey(Objeto,verbose_name="Objeto sobre el que se realiza el informe")
    nombre_res = models.CharField(max_length=30,verbose_name=("Nombre restaurador"))
    ape_res = models.CharField(max_length=50,verbose_name=("Apellidos del restaurador")) 
    proyecto = models.TextField(verbose_name=("Proyecto"))
    observaciones = models.TextField(verbose_name=("Observaciones extra sobre el objeto"))
    desarrollo = models.TextField(verbose_name=("Desarrollo"))
    fecha =  models.DateField(auto_now=True,verbose_name=("Fecha del informe"))  
    
    def __str__(self):
        return str(self.id) 
    class Meta:
        ordering = ["fecha"]
        verbose_name_plural = "Intervenciones de arqueología"
        
