from django.contrib import admin

from .models import Imagen

class ImagenAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion', 'creditos')

admin.site.register(Imagen, ImagenAdmin)