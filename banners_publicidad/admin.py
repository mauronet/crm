from django.contrib import admin

from .models import BannerPublicidad

class BannerPublicidadAdmin(admin.ModelAdmin):
	list_display = ('nombre','descripcion')
	search_fields = ('nombre','descripcion')

admin.site.register(BannerPublicidad, BannerPublicidadAdmin)
