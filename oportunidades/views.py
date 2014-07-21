from django.shortcuts import render, get_object_or_404

from franjas.models import Franja
from entidades.models import Entidad
from categorias.models import Categoria
from tags.models import Tag
from oportunidades.models import Oportunidad
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

def oportunidades_view(request,pagina=1):
	pagina = Pagina.objects.get(id=17)
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
				filters = filters | Q(nombre__icontains = palabraABuscar) | Q(descripcion__icontains = palabraABuscar)

			if len(franjasABuscar) > 0:
				filters = filters & Q(franjas__id__in = franjasABuscar)

			if len(entidadesABuscar) > 0:
				filters = filters & Q(entidades__id__in = entidadesABuscar)

			if len(categoriasABuscar) > 0:
				filters = filters & Q(categorias__id__in = categoriasABuscar)

			if len(tagsABuscar) > 0:
				filters = filters & Q(tags__id__in = tagsABuscar)

			listaOportunidades = Oportunidad.objects.filter(filters)
		else:
			listaOportunidades = Oportunidad.objects.filter()
	else:
		listaOportunidades = Oportunidad.objects.filter()

	numeroTotalOportunidades = len(listaOportunidades)
	paginator = Paginator(listaOportunidades, 5) #Cuantos items van por pagina

	paginas = []
	for numPagina in range(paginator.num_pages):
	    paginas += [str(numPagina+1)]

	try:
		page = int(pagina)
	except:
		page = 1
	try:
		listaOportunidadesPorPagina = paginator.page(page)
	except (EmptyPage, InvalidPage):
		listaOportunidadesPorPagina = paginator.page(paginator.num_pages)

	ctx = {
		'listaFranjas':listaFranjas,
		'listaEntidades':listaEntidades,
		'listaCategorias':listaCategorias,
		'listaTags':listaTags,
		'listaOportunidades':listaOportunidadesPorPagina,
		'palabraABuscar':palabraABuscar,
		'franjasABuscar':franjasABuscar,
		'entidadesABuscar':entidadesABuscar,
		'categoriasABuscar':categoriasABuscar,
		'tagsABuscar':tagsABuscar,
		'numeroTotalOportunidades':numeroTotalOportunidades,
		'paginas':paginas,
		'pagina':pagina,
	}


	return render(request, 'home/oportunidades.html',ctx)	

def oportunidad_view(request,id_oportunidad):
	pagina = Pagina.objects.get(id=18)
	oportunidad = get_object_or_404(Oportunidad, id=id_oportunidad)
	oportunidad.nombre = "<br>".join(oportunidad.nombre.split("\n"))	
	oportunidad.descripcion = "<br>".join(oportunidad.descripcion.split("\n"))	
	ctx = {
		'oportunidad':oportunidad,
		'pagina':pagina,
	}
	return render(request, 'home/oportunidad.html', ctx)

def nuevo_comentario_oportunidad_view(request):
	url = "/"
	if request.method=="POST":
		if "id_oportunidad" in request.POST and "txt_comentario" in request.POST and request.user.is_authenticated():
			try:
				oportunidad = Oportunidad.objects.get(id=request.POST['id_oportunidad'])
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
			oportunidad.comentarios.add(comentario.id)
			url = "/oportunidades/" + request.POST['id_oportunidad'] + "/"
	return HttpResponseRedirect(url)
