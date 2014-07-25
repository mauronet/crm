from django.shortcuts import render, get_object_or_404

from franjas.models import Franja
from entidades.models import Entidad
from categorias.models import Categoria
from tags.models import Tag
from eventos.models import Evento
from imagenes.models import Imagen
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage

from comentarios.models import Comentario
from estados_comentarios.models import EstadoComentario
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from userprofiles.models import UserProfile
from tipos_usuario.models import TipoUsuario
from django.http import HttpResponseRedirect
from paginas.models import Pagina
import pdb

def eventos_view(request,id_pagina=1):
	pagina = Pagina.objects.get(id=7)
	listaFranjas = Franja.objects.filter()
	listaEntidades = Entidad.objects.filter(activo=True)
	listaCategorias = Categoria.objects.filter()
	listaTags = Tag.objects.filter()

	palabraABuscar = ""
	franjasABuscar = []
	entidadesABuscar = []
	categoriasABuscar = []
	tagsABuscar = []

	if request.method=="POST":
		if "palabra" in request.POST:
			palabraABuscar = request.POST['palabra']
			franjasABuscar = request.POST.getlist('franjas[]')
			entidadesABuscar = request.POST.getlist('entidades[]')
			categoriasABuscar = request.POST.getlist('categorias[]')
			tagsABuscar = request.POST.getlist('tags[]')

			filters = Q()

			if palabraABuscar != "":
				filters = filters | Q(nombre__icontains = palabraABuscar) | Q(descripcion__icontains = palabraABuscar) | Q(lugar__icontains = palabraABuscar) 

			if len(franjasABuscar) > 0:
				filters = filters & Q(franjas__id__in = franjasABuscar)

			if len(entidadesABuscar) > 0:
				filters = filters & Q(entidades__id__in = entidadesABuscar)

			if len(categoriasABuscar) > 0:
				filters = filters & Q(categorias__id__in = categoriasABuscar)

			if len(tagsABuscar) > 0:
				filters = filters & Q(tags__id__in = tagsABuscar)

			listaEventos = Evento.objects.filter(filters).order_by("-inicio")
		else:
			listaEventos = Evento.objects.filter().order_by("-inicio")
	else:
		listaEventos = Evento.objects.filter().order_by("-inicio")

	numeroTotalEventos = len(listaEventos)
	paginator = Paginator(listaEventos, 5) #Cuantos items van por pagina

	paginas = []
	for numPagina in range(paginator.num_pages):
	    paginas += [str(numPagina+1)]

	try:
		page = int(id_pagina)
	except:
		page = 1
	try:
		listaEventosPorPagina = paginator.page(page)
	except (EmptyPage, InvalidPage):
		listaEventosPorPagina = paginator.page(paginator.num_pages)

	ctx = {
		'listaFranjas':listaFranjas,
		'listaEntidades':listaEntidades,
		'listaCategorias':listaCategorias,
		'listaTags':listaTags,
		'listaEventos':listaEventosPorPagina,
		'palabraABuscar':palabraABuscar,
		'franjasABuscar':franjasABuscar,
		'entidadesABuscar':entidadesABuscar,
		'categoriasABuscar':categoriasABuscar,
		'tagsABuscar':tagsABuscar,
		'numeroTotalEventos':numeroTotalEventos,
		'paginas':paginas,
		'pagina':pagina,
	}


	return render(request, 'home/eventos.html',ctx)	

def evento_view(request,id_evento):
	pagina = Pagina.objects.get(id=8)
	evento = get_object_or_404(Evento, id=id_evento)
	evento.nombre = "<br>".join(evento.nombre.split("\n"))	
	evento.descripcion = "<br>".join(evento.descripcion.split("\n"))	
	evento.lugar = "<br>".join(evento.lugar.split("\n"))	
	ctx = {
		'evento':evento,
		'pagina':pagina,
	}
	return render(request, 'home/evento.html', ctx)

def nuevo_comentario_evento_view(request):
	url = "/"
	if request.method=="POST":
		if "id_evento" in request.POST and "txt_comentario" in request.POST and request.user.is_authenticated():
			try:
				evento = Evento.objects.get(id=request.POST['id_evento'])
			except ObjectDoesNotExist:
				url = "/"
			comentario = Comentario()
			comentario.contenido = request.POST['txt_comentario']
			e = EstadoComentario.objects.get(id=1)
			comentario.estado = e
			comentario.fecha = datetime.today()
			user = request.user
			try:
				perfil = UserProfile.objects.get(user=user)
			except ObjectDoesNotExist:
				t = TipoUsuario.objects.get(id=2)
				perfil = UserProfile.objects.create(user=user,tipo=t)
				perfil.save()
			comentario.usuario = perfil
			comentario.save()
			evento.comentarios.add(comentario.id)
			url = "/eventos/" + request.POST['id_evento'] + "/"
			#pdb.set_trace()
	return HttpResponseRedirect(url)
