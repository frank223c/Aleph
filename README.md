[![codebeat badge](https://codebeat.co/badges/1b8469ca-00af-4265-93e2-3bce23b2c0f2)](https://codebeat.co/projects/github-com-usernameistakenlol-aleph-master)

# **PROYECTO ALEPH**

Aleph es una aplicación web creada con el framework Django para digitalizar la tarea de documentación museográfica.


---------------------------------------------------------

[Prueba](http://i.imgur.com/PDJ7839.gif)

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
