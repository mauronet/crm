from django.contrib import admin

from .models import Video

class VideoAdmin(admin.ModelAdmin):
	list_display = ('nombre','descripcion','creditos')
	filter_horizontal = ('categorias','tags','franjas','entidades')

admin.site.register(Video, VideoAdmin)