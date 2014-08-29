from django.contrib import admin
from .models import Suscriptor

class SuscriptorAdmin(admin.ModelAdmin):
	list_display = ('email','fecha_suscripcion')
	search_fields = ('email','fecha_suscripcion')

admin.site.register(Suscriptor, SuscriptorAdmin)