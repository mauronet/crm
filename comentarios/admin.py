from django.contrib import admin

from .models import Comentario

class ComentarioAdmin(admin.ModelAdmin):
	list_display = ('fecha','usuario','contenido','estado',)
	list_filter = ('estado',)
	list_editable = ('estado',)

admin.site.register(Comentario, ComentarioAdmin)
