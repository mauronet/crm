from django.contrib import admin

from .models import Fondo

class FondoAdmin(admin.ModelAdmin):
	list_display = ('nombre',)

admin.site.register(Fondo, FondoAdmin)