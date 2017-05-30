
**PROYECTO ALEPH**

---------------------------------------------------------
[Prueba](http://i.imgur.com/PDJ7839.gif)

1.Creación de entorno virtual e instalacion de requisitos para utilizar la aplicación

````python
pip install python-virtualenv
virtualenv
source env/bin/activate
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
````

2.Dirigirse a 127.0.0.1:8000 e iniciar sesión con un usuario válido.



**Aleph**

*Aleph es una aplicación web creada con el framework Django para digitalizar la tarea de documentación museográfica ,respetando la normativa ya vigente sobre
dicha tarea. La documentación es una tarea que conlleva varias funciones, desde registrar un objeto de inventario hasta crear un informe sobre
la conservación del mismo.

Está configurado para utilizar como DB Postgre y como backend de autenticación Active Directory*


