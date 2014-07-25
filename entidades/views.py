from django.shortcuts import render, get_object_or_404
from entidades.models import Entidad
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from paginas.models import Pagina

def entidades_view(request,id_pagina=1):
	pagina = Pagina.objects.get(id=5)
	listaIESAfiliadas = Entidad.objects.filter(activo=True, tipo=2)

	numeroTotalIES = len(listaIESAfiliadas)
	paginator = Paginator(listaIESAfiliadas, 2) #Cuantos items van por pagina

	paginas = []
	for numPagina in range(paginator.num_pages):
	    paginas += [str(numPagina+1)]

	try:
		page = int(id_pagina)
	except:
		page = 1
	try:
		listaIESAfiliadasPorPagina = paginator.page(page)
	except (EmptyPage, InvalidPage):
		listaIESAfiliadasPorPagina = paginator.page(paginator.num_pages)

	ctx = {
		'listaIESAfiliadas':listaIESAfiliadasPorPagina,
		'numeroTotalIES':numeroTotalIES,
		'paginas':paginas,
		'pagina':pagina,
	}

	#pdb.set_trace()

	return render(request, 'home/entidades.html',ctx)	

def entidad_view(request,id_entidad):
	pagina = Pagina.objects.get(id=4)
	ies = get_object_or_404(Entidad, id=id_entidad)
	ctx = {
		'ies':ies,
		'pagina':pagina,
	}
	return render(request, 'home/entidad.html', ctx)	

def ies_view(request,id_entidad):
	pagina = Pagina.objects.get(id=10)
	ies = get_object_or_404(Entidad, id=id_entidad)
	ies.leyenda = "<br>".join(ies.leyenda.split("\n"))	

	ctx = {
		'ies':ies,
		'pagina':pagina,
	}
	return render(request, 'home/ies.html', ctx)	

# API Key Google Maps: AIzaSyAhk1Town3jU_730V3qTIag1NmTLG2_t7U