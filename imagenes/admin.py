from django.contrib import admin

from .models import Imagen

class ImagenAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion', 'creditos', 'img_thumbnail')

admin.site.register(Imagen, ImagenAdmin)