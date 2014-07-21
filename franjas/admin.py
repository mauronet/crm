from django.contrib import admin

from .models import Franja

class FranjaAdmin(admin.ModelAdmin):
	list_display = ('nombre','descripcion')

admin.site.register(Franja, FranjaAdmin)