[![codebeat badge](https://codebeat.co/badges/1b8469ca-00af-4265-93e2-3bce23b2c0f2)](https://codebeat.co/projects/github-com-usernameistakenlol-aleph-master)
[![GPL Licence](https://badges.frapsoft.com/os/gpl/gpl.png?v=103)](https://opensource.org/licenses/GPL-3.0/)
[![Build Status](https://scrutinizer-ci.com/g/usernameistakenlol/Aleph/badges/build.png?b=master)](https://scrutinizer-ci.com/g/usernameistakenlol/Aleph/build-status/master)
[![Requirements Status](https://requires.io/github/usernameistakenlol/Aleph/requirements.svg?branch=master)](https://requires.io/github/usernameistakenlol/Aleph/requirements/?branch=master)

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c1e6a04326c24325af696abd266bff11)](https://www.codacy.com/app/carmen.morales.bonet/Aleph?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=usernameistakenlol/Aleph&amp;utm_campaign=Badge_Grade)

# **PROYECTO ALEPH**

Aleph es una aplicación web creada con Django para digitalizar la tarea de documentación museográfica.
![alt text](https://www.djangoproject.com/m/img/badges/djangomade124x25.gif 'Powered by Django')
---------------------------------------------------------

## ¿Cómo utilizarlo?

1.Creación de entorno virtual e instalacion de requisitos para utilizar la aplicación

````python
virtualenv <NombreEntornoVirtual>
source <NombreEntornoVirtual>/bin/activate
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
````

2.Abre tu navegador favorito y dirígete a la dirección 127.0.0.1:8000 

3.Iniciar sesión con un usuario válido.



**Cambios realizados**

*Arreglado problema con relaciones 

*Creada la parte de intervención de arqueología

*Probando autenticación con servidor AD de prueba

*Cambios y arreglos menores en templates y css

**TO DO**

[] Dockerizar la aplicación
