from django.contrib import admin

from .models import Programacion

class ProgramacionAdmin(admin.ModelAdmin):
	list_display = ('fecha','horario','programa','franja')
	search_fields = ('fecha', 'horario')

admin.site.register(Programacion, ProgramacionAdmin)
