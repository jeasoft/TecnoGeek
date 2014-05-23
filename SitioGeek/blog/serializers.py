from rest_framework import serializers
from .models import Entradas
from django.contrib.auth.models import User

class EntradaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Entradas
		fields = ('url','titulo','contenido','timestamp','imagen','usuario','votos',)
		
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url','username','email')

