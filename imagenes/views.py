from django.shortcuts import render, get_object_or_404
from imagenes.models import Imagen
from paginas.models import Pagina

def imagen_view(request,id_imagen):
	pagina = Pagina.objects.get(id=11)
	imagen = get_object_or_404(Imagen, id=id_imagen)
	imagen.descripcion = "<br>".join(imagen.descripcion.split("\n"))
	imagen.creditos = "<br>".join(imagen.creditos.split("\n"))
	ctx = {
		'imagen':imagen,
		'pagina':pagina,
	}
	return render(request, 'home/imagen.html', ctx)