from django.contrib import admin

from .models import EstadoComentario

class EstadoComentarioAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')

admin.site.register(EstadoComentario, EstadoComentarioAdmin)
