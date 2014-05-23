from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    titulo = models.CharField(max_length=140,unique=True)

    def __unicode__(self):
        return self.titulo

class Subcategoria(models.Model):
    nombre = models.CharField(max_length=20)

    def __unicode__(self):
        return self.nombre

class Entradas(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(blank=True, null=True, upload_to="img/entries/")
    usuario = models.ForeignKey(User)
    votos = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, related_name="categorias",blank=True,null=True)
    subcategoria = models.ForeignKey(Subcategoria,related_name="subcategoria",blank=True,null=True)

    def popular(self):
        return self.votos >= 10

    popular.boolean=True

    def votos_rosados(self):
        return 'http://placehold.it/200x100/E8117F/ffffff/&text=%d+votos' % self.votos

    def __unicode__(self):
       
        return "%s - %s" % (self.titulo,self.categoria,self.subcategoria)
