# Clase de Django UCS - 2025 

## participantes:
- [Yurley](https://github.com/Yursksf1)



## Instrucciones

### Crear el entorno virtual
```
virtualenv venv
```

### Activar el entorno virtual
```
\venv\Scripts\activate
```
importante notar que en la consola aparece el nombre entre parentesis 

(venv) C:\Users\Usuario\Dev\clase_django_2025>


### ver las librerias instaladas
```
pip freeze
```

### instalar django
```
pip install django 
```

```
pip install -r requirements.txt
```

### crear nuevo proyecto 
```
django-admin startproject mysite .
```
esto me crea la estructura del proyecto inicial


```
mysite/__init__.py 
mysite/asgi.py 
mysite/settings.py 
mysite/urls.py 
mysite/wsgi.py 
manage.py
```

### activar el servidor
```
python manage.py runserver
```
para apagar el servidor Ctrl + C

### crear la base de datos
```
python manage.py migrate
```
esto crea la base de dato ejecutando las migraciones (creacion de las tablas)

### crear un usuario admin
```
python manage.py createsuperuser
```
estamos creando el usuario administrador, se debe llenar la informacion como nombre, email, y password 