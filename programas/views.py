from django.shortcuts import render, get_object_or_404
from programas.models import Programa
from capitulos.models import Capitulo
from paginas.models import Pagina
from django.core.exceptions import ObjectDoesNotExist
from imagenes.models import Imagen

def programa_view(request,id_programa):
	pagina = Pagina.objects.get(id=20)
	programa = get_object_or_404(Programa, id=id_programa)
	programa.sinopsis = "<br>".join(programa.sinopsis.split("\n"))
	programa.video.visto += 1
	programa.video.save()
	ctx = {
		'programa':programa,
		'pagina':pagina,
	}
	return render(request, 'home/produccion.html', ctx)

def capitulo_view(request,id_programa,id_capitulo):
	pagina = Pagina.objects.get(id=20)

	try:
		programa = Programa.objects.get(id=id_programa)
		capitulo = Capitulo.objects.get(id=id_capitulo)
	except ObjectDoesNotExist:
		return HttpResponseRedirect('/')
	capitulo.descripcion = "<br>".join(capitulo.descripcion.split("\n"))
	capitulo.direccion = "<br>".join(capitulo.direccion.split("\n"))
	capitulo.produccion = "<br>".join(capitulo.produccion.split("\n"))
	capitulo.video.visto += 1
	capitulo.video.save()
	ctx = {
		'programa':programa,
		'capitulo':capitulo,
		'pagina':pagina,
	}
	return render(request, 'home/capitulo.html', ctx)

def imagen_view(request,id_programa,id_imagen):
	pagina = Pagina.objects.get(id=11)
	programa = get_object_or_404(Programa, id=id_programa)
	imagen = get_object_or_404(Imagen, id=id_imagen)
	imagen.descripcion = "<br>".join(imagen.descripcion.split("\n"))
	imagen.creditos = "<br>".join(imagen.creditos.split("\n"))
	ctx = {
		'imagen':imagen,
		'pagina':pagina,
		'programa':programa,
	}
	return render(request, 'home/imagenprograma.html', ctx)