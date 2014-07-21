from django.contrib import admin

from .models import EntradaBlog

class EntradaBlogAdmin(admin.ModelAdmin):
	list_display = ('titulo','lead','fecha')
	search_fields = ('titulo', 'lead','contenido')
	filter_horizontal = ('comentarios','categorias','tags','franjas','entidades','imagenes_adicionales','videos','documentos')

admin.site.register(EntradaBlog, EntradaBlogAdmin)
