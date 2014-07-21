from django.contrib import admin

from .models import Pagina

class PaginaAdmin(admin.ModelAdmin):
	list_display = ('nombre','descripcion')
	search_fields = ('nombre','descripcion')

admin.site.register(Pagina, PaginaAdmin)