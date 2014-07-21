from django.contrib import admin

from .models import Oportunidad

class OportunidadAdmin(admin.ModelAdmin):
	list_display = ('nombre','descripcion','fecha')
	search_fields = ('nombre', 'descripcion')
	filter_horizontal = ('comentarios','categorias','tags','franjas','entidades','imagenes_adicionales','videos','documentos')

admin.site.register(Oportunidad, OportunidadAdmin)