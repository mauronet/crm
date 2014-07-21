from django.shortcuts import render, get_object_or_404
from franjas.models import Franja
from entidades.models import Entidad
from categorias.models import Categoria
from tags.models import Tag
from videos.models import Video
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from paginas.models import Pagina

def videos_view(request,pagina):
	pagina = Pagina.objects.get(id=24)
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

			listaVideos = Video.objects.filter(filters)
		else:
			listaVideos = Video.objects.filter()
	else:
		listaVideos = Video.objects.filter()

	numeroTotalvideos = len(listaVideos)
	paginator = Paginator(listaVideos, 6) #Cuantos items van por pagina

	paginas = []
	for numPagina in range(paginator.num_pages):
	    paginas += [str(numPagina+1)]

	try:
		page = int(pagina)
	except:
		page = 1
	try:
		listaVideosPorPagina = paginator.page(page)
	except (EmptyPage, InvalidPage):
		listaVideosPorPagina = paginator.page(paginator.num_pages)

	ctx = {
		'listaFranjas':listaFranjas,
		'listaEntidades':listaEntidades,
		'listaCategorias':listaCategorias,
		'listaTags':listaTags,
		'listaVideos':listaVideosPorPagina,
		'palabraABuscar':palabraABuscar,
		'franjasABuscar':franjasABuscar,
		'entidadesABuscar':entidadesABuscar,
		'categoriasABuscar':categoriasABuscar,
		'tagsABuscar':tagsABuscar,
		'numeroTotalvideos':numeroTotalvideos,
		'paginas':paginas,
		'pagina':pagina,
	}

	#pdb.set_trace()

	return render(request, 'home/videos.html',ctx)	

def video_view(request,id_video):
	pagina = Pagina.objects.get(id=23)
	video = get_object_or_404(Video, id=id_video)
	video.descripcion = "<br>".join(video.descripcion.split("\n"))
	video.creditos = "<br>".join(video.creditos.split("\n"))
	ctx = {
		'video':video,
		'pagina':pagina,
	}
	return render(request, 'home/video.html', ctx)	
