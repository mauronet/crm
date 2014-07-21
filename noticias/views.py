from django.shortcuts import render, get_object_or_404
from franjas.models import Franja
from entidades.models import Entidad
from categorias.models import Categoria
from tags.models import Tag
from noticias.models import Noticia
from comentarios.models import Comentario
from estados_comentarios.models import EstadoComentario
from imagenes.models import Imagen
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage

from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from userprofiles.models import UserProfile
from tipos_usuario.models import TipoUsuario
from django.http import HttpResponseRedirect
from paginas.models import Pagina

import pdb

def noticias_view(request,pagina=1):
	pagina = Pagina.objects.get(id=15)
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
				filters = filters | Q(titulo__icontains = palabraABuscar) | Q(lead__icontains = palabraABuscar) | Q(contenido__icontains = palabraABuscar) 

			if len(franjasABuscar) > 0:
				filters = filters & Q(franjas__id__in = franjasABuscar)

			if len(entidadesABuscar) > 0:
				filters = filters & Q(entidades__id__in = entidadesABuscar)

			if len(categoriasABuscar) > 0:
				filters = filters & Q(categorias__id__in = categoriasABuscar)

			if len(tagsABuscar) > 0:
				filters = filters & Q(tags__id__in = tagsABuscar)

			listaNoticias = Noticia.objects.filter(filters)
		else:
			listaNoticias = Noticia.objects.filter()
	else:
		listaNoticias = Noticia.objects.filter()

	numeroTotalNoticias = len(listaNoticias)
	paginator = Paginator(listaNoticias, 5) #Cuantos items van por pagina

	paginas = []
	for numPagina in range(paginator.num_pages):
	    paginas += [str(numPagina+1)]

	try:
		page = int(pagina)
	except:
		page = 1
	try:
		listaNoticiasPorPagina = paginator.page(page)
	except (EmptyPage, InvalidPage):
		listaNoticiasPorPagina = paginator.page(paginator.num_pages)

	ctx = {
		'listaFranjas':listaFranjas,
		'listaEntidades':listaEntidades,
		'listaCategorias':listaCategorias,
		'listaTags':listaTags,
		'listaNoticias':listaNoticiasPorPagina,
		'palabraABuscar':palabraABuscar,
		'franjasABuscar':franjasABuscar,
		'entidadesABuscar':entidadesABuscar,
		'categoriasABuscar':categoriasABuscar,
		'tagsABuscar':tagsABuscar,
		'numeroTotalNoticias':numeroTotalNoticias,
		'paginas':paginas,
		'pagina':pagina,
	}


	return render(request, 'home/noticias.html',ctx)	

def noticia_view(request,id_noticia):
	pagina = Pagina.objects.get(id=14)
	noticia = get_object_or_404(Noticia, id=id_noticia)
	noticia.lead = "<br>".join(noticia.lead.split("\n"))	
	noticia.contenido = "<br>".join(noticia.contenido.split("\n"))
	ctx = {
		'noticia':noticia,
		'pagina':pagina,
	}
	return render(request, 'home/noticia.html', ctx)

def nuevo_comentario_noticia_view(request):
	url = "/"
	if request.method=="POST":
		if "id_noticia" in request.POST and "txt_comentario" in request.POST and request.user.is_authenticated():
			try:
				noticia = Noticia.objects.get(id=request.POST['id_noticia'])
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
			noticia.comentarios.add(comentario.id)
			url = "/noticias/" + request.POST['id_noticia'] + "/"
	return HttpResponseRedirect(url)
