from django.contrib import admin

from .models import Capitulo

class CapituloAdmin(admin.ModelAdmin):
	list_display = ('nombre','descripcion')

admin.site.register(Capitulo, CapituloAdmin)