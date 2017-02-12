# -*- coding: utf-8 -*-
# Creamdo el blog
#Todas las líneas que comienzan con from o import son líneas para agregar algo de otros archivos. Así que en vez de copiar y pegar las mismas cosas en cada archivo,
# podemos incluir algunas partes con from... import .... 


from django.db import models
from django.utils import timezone


# Create your models here.

#esta línea define nuestro modelo (es un objeto).
#class es una palabra clave que indica que estamos definiendo un objeto.
#Post es el nombre de nuestro modelo. Podemos darle un nombre diferente (pero debemos evitar espacios en blanco y caracteres especiales). Empieza siempre el nombre de una clase con una letra mayúscula.
#models.Model significa que Post es un modelo de Django, así Django sabe que debe guardarlo en la base de datos.



class Post(models.Model):

#Ahora definimos las propiedades: Para ello tenemos que definir un tipo
#de campo (¿es texto? ¿un número? ¿una fecha? ¿una relación con otro 
#objeto - es decir, un usuario?).


    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

# models.DateTimeField - este es una fecha y hora.
#modelos.ForeignKey - este es un vínculo con otro modelo.


#Es justo el método publish que mencionábamos antes. def 
#significa que es una función/método y publish es el nombre del método.

    def publish(self):
        self.published_date = timezone.now()
        self.save()

# __str__ se usa con frecuencia en Python
#Los métodos suelen devolver algo, en inglés: return.
#En este escenario, cuando llamamos a __str__() obtendremos un 
#texto (string) con un título de Post.


    def __str__(self):
        return self.title

