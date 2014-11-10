from django.contrib.auth.models import User
from django.db import models
from django.template import defaultfilters


# Aplicaciones de 3ros
from tinymce.models import HTMLField
from smart_selects.db_fields import ChainedForeignKey 

class Categoria(models.Model):
    titulo = models.CharField(max_length=140,unique=True)
    slug = models.SlugField(max_length=140)

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.titulo)
        super(Categoria, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.titulo


class Subcategoria(models.Model):
    nombre = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    categoria = models.ForeignKey(Categoria)

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.nombre)
        super(Subcategoria, self).save(*args, **kwargs)

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
    subcategoria = ChainedForeignKey(
        Subcategoria,
        chained_field="categoria",
        chained_model_field = "categoria",
        show_all = False,
        auto_choose=True,
       # related_name="subcategoria",blank=True,null=True
    )

    def popular(self):
        return self.votos >= 10

    popular.boolean=True

    def __unicode__(self):
        return "%s" % (self.titulo)
