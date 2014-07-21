from django.contrib import admin
from .models import TipoVideo

class TipoVideoAdmin(admin.ModelAdmin):
	list_display = ('nombre',)

admin.site.register(TipoVideo, TipoVideoAdmin)
