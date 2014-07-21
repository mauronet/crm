from django.contrib import admin
from banner_sizes.models import BannerSize

class BannerSizeAdmin(admin.ModelAdmin):
	list_display = ('ancho','alto')

admin.site.register(BannerSize, BannerSizeAdmin)
		
