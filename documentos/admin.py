from django.contrib import admin

from  .models import Documento

class DocumentoAdmin(admin.ModelAdmin):
	list_display = ('nombre','descripcion','file_link')
	search_fields = ('nombre', 'descripcion', 'archivo')

admin.site.register(Documento, DocumentoAdmin)
