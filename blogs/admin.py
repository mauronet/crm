from django.contrib import admin

from .models import Blog

class BlogAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'entidad')
	search_fields = ('nombre', 'entidad')

admin.site.register(Blog, BlogAdmin)