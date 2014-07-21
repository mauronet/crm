from django.contrib import admin

from .models import HorarioProgramacion

class HorarioProgramacionAdmin(admin.ModelAdmin):
	list_display = ('manana','tarde_noche')

admin.site.register(HorarioProgramacion, HorarioProgramacionAdmin)