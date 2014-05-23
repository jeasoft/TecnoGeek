from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render_to_response,get_object_or_404, render
from django.template.loader import get_template
from models import *
from datetime import datetime
from django.core.urlresolvers import reverse
from django.template import RequestContext, Context
from forms import *
from django.contrib.auth.decorators import login_required


def home(request):
	categorias = Categoria.objects.all()
	subcategorias = Subcategoria.objects.all()
	entrada = Entradas.objects.order_by("-timestamp").all()
	paginator = Paginator(entrada,5)
	
	try: pagina = int(request.GET.get("page",'1'))
	except ValueError: pagina = 1
	
	try:
		entrada = paginator.page(pagina)
	except (InvalidPage, EmptyPage):
		entrada = paginator.page(paginator.num_page)

	template = "index.html"
	return render(request,template,locals())

def categoria(request,id_categoria):
    categorias = Categoria.objects.all()
    subcategorias = Subcategoria.objects.all()
    cat = get_object_or_404(Categoria,pk = id_categoria)
    entrada = Entradas.objects.filter(categoria = cat).order_by("-timestamp")
    template = "index.html"
    return render(request,template,locals())

def subcategoria(request,id_scategoria):
    categorias = Categoria.objects.all()
    subcategorias = Subcategoria.objects.all()
    scat = get_object_or_404(Subcategoria,pk = id_scategoria)
    entrada = Entradas.objects.filter(subcategoria = scat)
    template = "index.html"
    return render(request,template,locals())

def post(request, pk):
	post = Entradas.objects.get(pk = pk)
	categorias = Categoria.objects.all()
	subcategorias = Subcategoria.objects.all()
	template = "post.html"
	return render(request,template,locals())

def acerca(request):
	categorias = Categoria.objects.all()
	subcategorias = Subcategoria.objects.all() 
	template = "acerca_de.html"
	return render(request,template,locals())

@login_required
def minus(request,entrada_id):
    posts = get_object_or_404(Entradas,pk=entrada_id)
    posts.votos = posts.votos - 1
    posts.save()
    return HttpResponseRedirect("/")
	
@login_required
def plus(request,entrada_id):
    posts = get_object_or_404(Entradas,pk=entrada_id)
    posts.votos = posts.votos + 1
    posts.save()
    return HttpResponseRedirect("/")

@login_required
def add(request):
    categorias=Categoria.objects.all()
    subcategorias = Subcategoria.objects.all()
    if request.method == "POST":
        form = EntradaForm(request.POST)
        if form.is_valid():
            entrada=form.save(commit=False)
            entrada.usuario=request.user
            entrada.save()
            HttpResponseRedirect("/")
    else:
        form=EntradaForm()
    template = "form.html"
    return render_to_response(template,
                             context_instance=RequestContext(request,locals()))

from .serializers import EntradaSerializer,UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User


class EntradaViewSet(viewsets.ModelViewSet):
    queryset = Entradas.objects.all()
    serializer_class = EntradaSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer