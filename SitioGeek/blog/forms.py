from django import forms
from django.forms import ModelForm
from models import *

class EntradaForm(ModelForm):
	class Meta:
		model = Entradas
		exclude = ("votos","usuario")
