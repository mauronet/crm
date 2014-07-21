from django.contrib import admin

from .models import Noticia

class NoticiaAdmin(admin.ModelAdmin):
	list_display = ('titulo','lead','fecha')
	search_fields = ('titulo','lead','contenido')
	filter_horizontal = ('comentarios','categorias','tags','franjas','entidades','imagenes_adicionales','videos','documentos')

admin.site.register(Noticia, NoticiaAdmin)

