from django.contrib import admin

from .models import ElementoCarrusel

class ElementoCarruselAdmin(admin.ModelAdmin):
	list_display = ('id',)

admin.site.register(ElementoCarrusel, ElementoCarruselAdmin)

