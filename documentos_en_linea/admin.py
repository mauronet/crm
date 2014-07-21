from django.contrib import admin

from  .models import DocumentoEnLinea

class DocumentoEnLineaAdmin(admin.ModelAdmin):
	list_display = ('nombre','descripcion')

admin.site.register(DocumentoEnLinea, DocumentoEnLineaAdmin)
