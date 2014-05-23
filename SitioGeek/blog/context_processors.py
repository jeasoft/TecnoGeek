# -*- coding: utf-8 -*-
from random import choice
frases =['Alegria de un Backend','Frontend se basa en diseño','Lo mejor de las Web',
'Backendpro']

def ejemplo(request):
    return {'frase': choice(frases)}