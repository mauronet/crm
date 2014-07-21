from django.contrib import admin

from .models import TipoUsuario

class TipoUsuarioAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')

admin.site.register(TipoUsuario, TipoUsuarioAdmin)
