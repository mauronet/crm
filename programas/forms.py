from django import forms

class AdminProgramaForm(forms.Form):
	nombre = models.CharField(max_length=255)
	sinopsis = models.TextField(blank=True)
	video = models.ForeignKey(Video, null=True, blank=True)
	banner = models.ImageField(upload_to="banners", blank=True) 
	color_fondo = models.CharField(max_length=6, blank=True)
	color_linea = models.CharField(max_length=6, blank=True)
	color_letra = models.CharField(max_length=6, blank=True)
	tipo_letra = models.CharField(max_length=30, blank=True)
	capitulos = models.ManyToManyField(Capitulo, blank=True)
	imagenes = models.ManyToManyField(Imagen, blank=True)