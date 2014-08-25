from django.contrib import admin

from .models import NoticiasDestacadas

class NoticiasDestacadasAdmin(admin.ModelAdmin):
	list_display = ('id',)
	filter_horizontal = ('noticias',)

admin.site.register(NoticiasDestacadas, NoticiasDestacadasAdmin)
