from django.contrib import admin

from .models import Carrusel

class CarruselAdmin(admin.ModelAdmin):
	list_display = ('id',)
	filter_horizontal = ('noticias','oportunidades','eventos','entradas')

admin.site.register(Carrusel, CarruselAdmin)

