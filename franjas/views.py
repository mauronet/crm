from django.shortcuts import render, get_object_or_404
from franjas.models import Franja
from paginas.models import Pagina
import pdb

def franja_view(request,nombre):
	pagina = Pagina.objects.get(id=9)
	franja = get_object_or_404(Franja, nombre=nombre)
	franja.descripcion = "<br>".join(franja.descripcion.split("\n"))
	ctx = {
		'franja':franja,
		'pagina':pagina,
	}
	return render(request, 'home/franja.html', ctx)