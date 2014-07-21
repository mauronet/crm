from django.shortcuts import render, get_object_or_404
from franjas.models import Franja
from entidades.models import Entidad
from categorias.models import Categoria
from tags.models import Tag
from blogs.models import Blog
from entradas_blogs.models import EntradaBlog
from imagenes.models import Imagen
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage

from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from userprofiles.models import UserProfile
from tipos_usuario.models import TipoUsuario
from django.http import HttpResponseRedirect
from comentarios.models import Comentario
from estados_comentarios.models import EstadoComentario
from paginas.models import Pagina

import pdb

def blog_view(request,id_blog,pagina):
	pagina = Pagina.objects.get(id=3)
	blog = Blog.objects.get(id=id_blog)
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

			filters = filters & Q(blog__id=id_blog)

			listaEntradasBlog = EntradaBlog.objects.filter(filters)
		else:
			listaEntradasBlog = EntradaBlog.objects.filter(blog__id=id_blog)
	else:
		listaEntradasBlog = EntradaBlog.objects.filter(blog__id=id_blog)

	numeroTotalEntradasBlog = len(listaEntradasBlog)
	paginator = Paginator(listaEntradasBlog, 5) #Cuantos items van por pagina

	paginas = []
	for numPagina in range(paginator.num_pages):
	    paginas += [str(numPagina+1)]

	try:
		page = int(pagina)
	except:
		page = 1
	try:
		listaEntradasBlogPorPagina = paginator.page(page)
	except (EmptyPage, InvalidPage):
		listaEntradasBlogPorPagina = paginator.page(paginator.num_pages)

	ctx = {
		'blog':blog,
		'listaFranjas':listaFranjas,
		'listaEntidades':listaEntidades,
		'listaCategorias':listaCategorias,
		'listaTags':listaTags,
		'listaEntradasBlog':listaEntradasBlogPorPagina,
		'palabraABuscar':palabraABuscar,
		'franjasABuscar':franjasABuscar,
		'entidadesABuscar':entidadesABuscar,
		'categoriasABuscar':categoriasABuscar,
		'tagsABuscar':tagsABuscar,
		'numeroTotalEntradasBlog':numeroTotalEntradasBlog,
		'paginas':paginas,
		'pagina':pagina,
	}
	return render(request, 'home/blog.html',ctx)	

def entrada_blog_view(request,id_entrada):
	pagina = Pagina.objects.get(id=6)
	entrada_blog = get_object_or_404(EntradaBlog, id=id_entrada)
	entrada_blog.lead = "<br>".join(entrada_blog.lead.split("\n"))	
	entrada_blog.contenido = "<br>".join(entrada_blog.contenido.split("\n"))	
	blogs = entrada_blog.blog_set.all()	
	blog = blogs[0]
	ctx = {
		'blog':blog,
		'entrada_blog':entrada_blog,
		'pagina':pagina,
	}
	return render(request, 'home/entrada_blog.html', ctx)

def nuevo_comentario_entrada_blog_view(request):
	url = "/"
	if request.method=="POST":
		if "id_entrada_blog" in request.POST and "txt_comentario" in request.POST and request.user.is_authenticated():
			try:
				entrada_blog = EntradaBlog.objects.get(id=request.POST['id_entrada_blog'])
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
			entrada_blog.comentarios.add(comentario.id)
			url = "/blogs/entradas/" + request.POST['id_entrada_blog'] + "/"
	return HttpResponseRedirect(url)
