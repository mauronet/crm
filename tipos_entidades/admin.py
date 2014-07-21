from django.contrib import admin

from .models import TipoEntidad

class TipoEntidadAdmin(admin.ModelAdmin):
	list_display = ('nombre','descripcion')

admin.site.register(TipoEntidad, TipoEntidadAdmin)
