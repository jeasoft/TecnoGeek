from django.contrib import admin
from blog.models import Entradas, Categoria,Subcategoria
from actions import export_as_csv


class EntradaAdmin(admin.ModelAdmin):
#	list_display = ('titulo','categoria','subcategoria','votos','usuario','popular')
#	list_filter=('usuario','categoria','subcategoria',)
#	search_fields = ('categoria__titulo','usuario__email',)
#	list_editable = ('categoria','subcategoria','titulo',)#puedo poner el contenito tambien 
#	actions = [export_as_csv]
#	list_display_links = ('usuario',)
#	raw_id_fields = ('categoria','usuario','subcategoria',)
    pass

class EntradaInline(admin.StackedInline):
#	model = Entradas
#	extra = 3
#	raw_id_fields = ('usuario',)
    pass

class CategoriaAdmin(admin.ModelAdmin):
#	inlines = [EntradaInline]
#	actions = [export_as_csv]
    exclude = ["slug",]

class SubcategoriaAdmin(admin.ModelAdmin):
    exclude = ["slug",]

admin.site.register(Entradas,EntradaAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Subcategoria, SubcategoriaAdmin)

