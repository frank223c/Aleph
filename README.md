
**PROYECTO ALEPH**

- En el directorio **Esquemas** estará todo lo relacionado con la especificación y el E-R ó UML de la base de datos
del proyecto djangoMca.

- En el directorio **Fondos** estará el proyecto de django y su codigo


---------------------------------------------------------
[Prueba](http://i.imgur.com/PDJ7839.gif)

Creación de entorno virtual e instalacion de requisitos para utilizar la aplicación

````python
pip install python-virtualenv
virtualenv
source env/bin/activate
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
````

**Versión 2.0 **

Prototipo inicial del proyecto Aleph, el proyecto consiste en digitalizar toda la información
de los objetos residentes en el mismo y a la conservación de las piezas. El hecho de que la documentación museográfica sea tan extensa
necesita una solución informatizada, por ello para mi proyecto final de ASIR se creó este prototipo.

Está configurado para utilizar como DB Postgre y como backend de autenticación Active Directory.


