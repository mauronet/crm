from django.contrib import admin

from .models import Blog

class BlogAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'entidad','administrador')
	search_fields = ('nombre', 'entidad','administrador')

admin.site.register(Blog, BlogAdmin)