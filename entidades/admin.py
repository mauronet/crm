from django.contrib import admin

from .models import Entidad

class EntidadAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'ciudad', 'telefonos','email','contacto')

admin.site.register(Entidad, EntidadAdmin)