from django.shortcuts import render
from imagenes.models import Imagen
from videos.models import Video
from documentos.models import Documento
from programas.models import Programa
from capitulos.models import Capitulo
from blogs.models import Blog
from entradas_blogs.models import EntradaBlog
from comentarios.models import Comentario
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from canalzoom.settings import LOGIN_URL
from django.core.exceptions import ObjectDoesNotExist
from userprofiles.models import UserProfile
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from admin_entidad.forms import addImagenForm
from admin_entidad.forms import addVideoForm
from admin_entidad.forms import addDocumentoForm
from admin_entidad.forms import addProgramaForm
from admin_entidad.forms import addCapituloForm
from admin_entidad.forms import addEntradaBlogForm
from admin_entidad.forms import ComentarioForm
from django import forms
from datetime import datetime
from django.forms.models import modelformset_factory
import pdb

def getPerfil(user):
	try:
		perfil = UserProfile.objects.get(user=user)
	except ObjectDoesNotExist:
		t = TipoUsuario.objects.get(id=2)
		perfil = UserProfile.objects.create(user=user,tipo=t)
		perfil.save()
	return perfil

@login_required(login_url=LOGIN_URL)
def adminentidad_index_view(request):
	perfil = getPerfil(request.user)
	if perfil.tipo.id == 3:
		return render(request, 'adminEntidad/index.html')
	else:
		return HttpResponseRedirect('/')

@login_required(login_url=LOGIN_URL)
def adminentidad_imagenes_view(request, page):
	perfil = getPerfil(request.user)
	if perfil.tipo.id == 3:
		lista_imagenes = Imagen.objects.filter(creado_por=perfil.entidad.id).order_by('-id')
		paginator = Paginator(lista_imagenes, 10) #Imagenes por pagina
		try:
			page = int(page)
		except:
			page = 1
		try:
			imagenes = paginator.page(page)
		except (EmptyPage, InvalidPage):
			imagenes = paginator.page(paginator.num_pages)
		ctx = {
			'imagenes': imagenes,
		}
		return render(request, 'adminEntidad/imagenes.html',ctx)
	else:
		return HttpResponseRedirect('/')

@login_required(login_url=LOGIN_URL)
def add_imagen_view(request):
	perfil = getPerfil(request.user)
	if perfil.tipo.id == 3:
		info=""
		if request.method == "POST":
			form = addImagenForm(request.POST,request.FILES)
			if form.is_valid():
				add = form.save(commit=False)
				add.creado_por = perfil.entidad
				add.save() # Guardamos la informacion
				#form.save_m2m() # Guarda las relaciones de ManyToMany
				#return HttpResponseRedirect('/adminEntidad/edit/imagen/%s'%add.id)
				return HttpResponseRedirect('/adminEntidad/imagenes/page/1/')
		else:
			form = addImagenForm()
		ctx = {
			'form':form,
			'informacion':info,
		}
		return render(request,'adminEntidad/imagen.html', ctx)
	else:
		return HttpResponseRedirect('/')

@login_required(login_url=LOGIN_URL)
def edit_imagen_view(request, id_img):
	perfil = getPerfil(request.user)
	if perfil.tipo.id == 3:
		img = Imagen.objects.get(pk=id_img)
		info=""
		if request.method == "POST":
			form = addImagenForm(request.POST,request.FILES,instance=img)
			if form.is_valid():
				edit_prod = form.save(commit=False)
				edit_prod.save()
				#return HttpResponseRedirect('/adminEntidad/edit/imagen/%s'%edit_prod.id)
				return HttpResponseRedirect('/adminEntidad/imagenes/page/1/')
		else:
			form = addImagenForm(instance=img)
		ctx = {
			'form':form,
			'informacion':info,
		}
		return render(request,'adminEntidad/imagen.html',ctx)
	else:
		return HttpResponseRedirect('/')


@login_required(login_url=LOGIN_URL)
def adminentidad_videos_view(request, page):
	perfil = getPerfil(request.user)
	if perfil.tipo.id == 3:
		lista_videos = Video.objects.filter(creado_por=perfil.entidad.id).order_by('-id')
		paginator = Paginator(lista_videos, 10) #videos por pagina
		try:
			page = int(page)
		except:
			page = 1
		try:
			videos = paginator.page(page)
		except (EmptyPage, InvalidPage):
			videos = paginator.page(paginator.num_pages)
		ctx = {
			'videos': videos,
		}
		return render(request, 'adminEntidad/videos.html',ctx)
	else:
		return HttpResponseRedirect('/')

@login_required(login_url=LOGIN_URL)
def add_video_view(request):
	perfil = getPerfil(request.user)
	if perfil.tipo.id == 3:
		info=""
		if request.method == "POST":
			form = addVideoForm(request.POST,request.FILES)
			if form.is_valid():
				add = form.save(commit=False)
				add.creado_por = perfil.entidad
				add.save() # Guardamos la informacion
				#form.save_m2m() # Guarda las relaciones de ManyToMany
				#return HttpResponseRedirect('/adminEntidad/edit/video/%s'%add.id)
				return HttpResponseRedirect('/adminEntidad/videos/page/1/')
		else:
			form = addVideoForm()
		ctx = {
			'form':form,
			'informacion':info,
		}
		return render(request,'adminEntidad/video.html', ctx)
	else:
		return HttpResponseRedirect('/')

@login_required(login_url=LOGIN_URL)
def edit_video_view(request, id_img):
	perfil = getPerfil(request.user)
	if perfil.tipo.id == 3:
		img = Video.objects.get(pk=id_img)
		info=""
		if request.method == "POST":
			form = addVideoForm(request.POST,request.FILES,instance=img)
			if form.is_valid():
				edit_prod = form.save(commit=False)
				edit_prod.save()
				#return HttpResponseRedirect('/adminEntidad/edit/video/%s'%edit_prod.id)
				return HttpResponseRedirect('/adminEntidad/videos/page/1/')
		else:
			form = addVideoForm(instance=img)
		ctx = {
			'form':form,
			'informacion':info,
		}
		return render(request,'adminEntidad/video.html',ctx)
	else:
		return HttpResponseRedirect('/')


@login_required(login_url=LOGIN_URL)
def adminentidad_documentos_view(request, page):
	perfil = getPerfil(request.user)
	if perfil.tipo.id == 3:
		lista_documentos = Documento.objects.filter(creado_por=perfil.entidad.id).order_by('-id')
		paginator = Paginator(lista_documentos, 10) #documentos por pagina
		try:
			page = int(page)
		except:
			page = 1
		try:
			documentos = paginator.page(page)
		except (EmptyPage, InvalidPage):
			documentos = paginator.page(paginator.num_pages)
		ctx = {
			'documentos': documentos,
		}
		return render(request, 'adminEntidad/documentos.html',ctx)
	else:
		return HttpResponseRedirect('/')

@login_required(login_url=LOGIN_URL)
def add_documento_view(request):
	perfil = getPerfil(request.user)
	if perfil.tipo.id == 3:
		info=""
		if request.method == "POST":
			form = addDocumentoForm(request.POST,request.FILES)
			if form.is_valid():
				add = form.save(commit=False)
				add.creado_por = perfil.entidad
				add.save() # Guardamos la informacion
				#form.save_m2m() # Guarda las relaciones de ManyToMany
				#return HttpResponseRedirect('/adminEntidad/edit/documento/%s'%add.id)
				return HttpResponseRedirect('/adminEntidad/documentos/page/1/')
		else:
			form = addDocumentoForm()
		ctx = {
			'form':form,
			'informacion':info,
		}
		return render(request,'adminEntidad/documento.html', ctx)
	else:
		return HttpResponseRedirect('/')

@login_required(login_url=LOGIN_URL)
def edit_documento_view(request, id_img):
	perfil = getPerfil(request.user)
	if perfil.tipo.id == 3:
		img = Documento.objects.get(pk=id_img)
		info=""
		if request.method == "POST":
			form = addDocumentoForm(request.POST,request.FILES,instance=img)
			if form.is_valid():
				edit_prod = form.save(commit=False)
				edit_prod.save()
				#return HttpResponseRedirect('/adminEntidad/edit/documento/%s'%edit_prod.id)
				return HttpResponseRedirect('/adminEntidad/documentos/page/1/')
		else:
			form = addDocumentoForm(instance=img)
		ctx = {
			'form':form,
			'informacion':info,
		}
		return render(request,'adminEntidad/documento.html',ctx)
	else:
		return HttpResponseRedirect('/')


@login_required(login_url=LOGIN_URL)
def adminentidad_programas_view(request):
	perfil = getPerfil(request.user)
	if perfil.tipo.id == 3:
		lista_programas = Programa.objects.filter(entidad=perfil.entidad.id).order_by('-id')
		ctx = {
			'programas': lista_programas,
		}
		return render(request, 'adminEntidad/programas.html',ctx)
	else:
		return HttpResponseRedirect('/')

@login_required(login_url=LOGIN_URL)
def edit_programa_view(request, id_img):
	perfil = getPerfil(request.user)
	if perfil.tipo.id == 3:
		try:
			img = Programa.objects.get(pk=id_img, entidad=perfil.entidad.id)
		except ObjectDoesNotExist:
			return HttpResponseRedirect('/adminEntidad/')	
		info=""
		if request.method == "POST":
			form = addProgramaForm(request.POST,request.FILES,instance=img)
			if form.is_valid():
				edit_prod = form.save(commit=False)
				edit_prod.save()
				form.save_m2m() # Guarda las relaciones de ManyToMany
				return HttpResponseRedirect('/adminEntidad/programas/')
		else:
			form = addProgramaForm(instance=img)
		form.fields['imagenes'] = forms.ModelMultipleChoiceField(queryset=Imagen.objects.filter(creado_por=perfil.entidad.id))
		form.fields['video'] = forms.ModelChoiceField(queryset=Video.objects.filter(creado_por=perfil.entidad.id))
		idPrograma = id_img
		ctx = {
			'form':form,
			'informacion':info,
			'idPrograma':idPrograma,
		}
		return render(request,'adminEntidad/programa.html',ctx)
	else:
		return HttpResponseRedirect('/')

@login_required(login_url=LOGIN_URL)
def adminentidad_capitulos_view(request,id_prg):
	perfil = getPerfil(request.user)
	if perfil.tipo.id == 3:
		try:
			prg = Programa.objects.get(pk=id_prg, entidad=perfil.entidad.id)
		except ObjectDoesNotExist:
			return HttpResponseRedirect('/adminEntidad/')
		ctx = {
			'programa': prg,
		}
		return render(request, 'adminEntidad/capitulos.html',ctx)
	else:
		return HttpResponseRedirect('/')


@login_required(login_url=LOGIN_URL)
def add_capitulo_view(request, id_prg):
	perfil = getPerfil(request.user)
	if perfil.tipo.id == 3:
		info=""
		try:
			prg = Programa.objects.get(pk=id_prg, entidad=perfil.entidad.id)
		except ObjectDoesNotExist:
			return HttpResponseRedirect('/adminEntidad/')
		if request.method == "POST":
			form = addCapituloForm(request.POST,request.FILES)
			if form.is_valid():
				add = form.save(commit=False)
				add.save()
				prg.capitulos.add(add)
				prg.save()
				return HttpResponseRedirect('/adminEntidad/programas/%s/capitulos/'%id_prg)
		else:
			form = addCapituloForm()
		form.fields['video'] = forms.ModelChoiceField(queryset=Video.objects.filter(creado_por=perfil.entidad.id))
		ctx = {
			'form':form,
			'programa':prg,
			'informacion':info,
		}
		return render(request,'adminEntidad/capitulo.html', ctx)
	else:
		return HttpResponseRedirect('/')

@login_required(login_url=LOGIN_URL)
def edit_capitulo_view(request, id_cap, id_prg):
	perfil = getPerfil(request.user)
	if perfil.tipo.id == 3:
		info=""
		try:
			cap = Capitulo.objects.get(pk=id_cap)
			prg = Programa.objects.get(pk=id_prg, entidad=perfil.entidad.id)
		except ObjectDoesNotExist:
			return HttpResponseRedirect('/adminEntidad/')
		if request.method == "POST":
			form = addCapituloForm(request.POST,request.FILES,instance=cap)
			if form.is_valid():
				edit_prod = form.save(commit=False)
				edit_prod.save()
				return HttpResponseRedirect('/adminEntidad/programas/%s/capitulos/'%id_prg)
		else:
			form = addCapituloForm(instance=cap)
		form.fields['video'] = forms.ModelChoiceField(queryset=Video.objects.filter(creado_por=perfil.entidad.id))
		ctx = {
			'form':form,
			'informacion':info,
			'programa':prg,
		}
		return render(request,'adminEntidad/capitulo.html',ctx)
	else:
		return HttpResponseRedirect('/')

@login_required(login_url=LOGIN_URL)
def adminentidad_blogs_view(request):
	perfil = getPerfil(request.user)
	if perfil.tipo.id == 3:
		lista_blogs = Blog.objects.filter(entidad=perfil.entidad.id).order_by('-id')
		ctx = {
			'blogs': lista_blogs,
		}
		return render(request, 'adminEntidad/blogs.html',ctx)
	else:
		return HttpResponseRedirect('/')

@login_required(login_url=LOGIN_URL)
def adminentidad_entradas_blog_view(request, id_blog, page):
	perfil = getPerfil(request.user)
	if perfil.tipo.id == 3:
		try:
			blog = Blog.objects.get(id=id_blog)
		except ObjectDoesNotExist:
			return HttpResponseRedirect('/adminEntidad/')
		entradas = blog.entradas.all().order_by('-id')
		paginator = Paginator(entradas, 10) #entradas por pagina
		try:
			page = int(page)
		except:
			page = 1
		try:
			entradas = paginator.page(page)
		except (EmptyPage, InvalidPage):
			entradas = paginator.page(paginator.num_pages)
		ctx = {
			'entradas': entradas,
			'blog': blog,
		}
		return render(request, 'adminEntidad/entradas.html',ctx)
	else:
		return HttpResponseRedirect('/')

@login_required(login_url=LOGIN_URL)
def add_entrada_view(request, id_blog):
	perfil = getPerfil(request.user)
	if perfil.tipo.id == 3:
		info=""
		try:
			blog = Blog.objects.get(pk=id_blog, entidad=perfil.entidad.id)
		except ObjectDoesNotExist:
			return HttpResponseRedirect('/adminEntidad/')
		if request.method == "POST":
			form = addEntradaBlogForm(request.POST,request.FILES)
			if form.is_valid():
				add = form.save(commit=False)
				add.fecha = datetime.today()
				add.save()
				form.save_m2m() # Guarda las relaciones de ManyToMany
				blog.entradas.add(add)
				blog.save()
				return HttpResponseRedirect('/adminEntidad/blogs/%s/entradas/page/1/'%id_blog)
		else:
			form = addEntradaBlogForm()
		form.fields['imagen_principal']  = forms.ModelChoiceField(queryset=Imagen.objects.filter(creado_por=perfil.entidad.id))
		form.fields['imagenes_adicionales'] = forms.ModelMultipleChoiceField(queryset=Imagen.objects.filter(creado_por=perfil.entidad.id))
		form.fields['videos']  = forms.ModelMultipleChoiceField(queryset=Video.objects.filter(creado_por=perfil.entidad.id))
		form.fields['documentos']  = forms.ModelMultipleChoiceField(queryset=Documento.objects.filter(creado_por=perfil.entidad.id))
		ctx = {
			'form':form,
			'blog':blog,
			'informacion':info,
		}
		return render(request,'adminEntidad/entrada.html', ctx)
	else:
		return HttpResponseRedirect('/')

@login_required(login_url=LOGIN_URL)
def edit_entrada_view(request, id_entrada, id_blog):
	perfil = getPerfil(request.user)
	if perfil.tipo.id == 3:
		info=""
		try:
			entradaBlog = EntradaBlog.objects.get(pk=id_entrada)
			blog = Blog.objects.get(pk=id_blog, entidad=perfil.entidad.id)
		except ObjectDoesNotExist:
			return HttpResponseRedirect('/adminEntidad/')
		if request.method == "POST":
			form = addEntradaBlogForm(request.POST,request.FILES,instance=entradaBlog)
			if form.is_valid():
				edit_entrada = form.save(commit=False)
				edit_entrada.fecha = datetime.today()
				edit_entrada.save()
				form.save_m2m() # Guarda las relaciones de ManyToMany
				return HttpResponseRedirect('/adminEntidad/blogs/%s/entradas/page/1/'%id_blog)
		else:
			form = addEntradaBlogForm(instance=entradaBlog)
		form.fields['imagen_principal']  = forms.ModelChoiceField(queryset=Imagen.objects.filter(creado_por=perfil.entidad.id))
		form.fields['imagenes_adicionales'] = forms.ModelMultipleChoiceField(queryset=Imagen.objects.filter(creado_por=perfil.entidad.id))
		form.fields['videos']  = forms.ModelMultipleChoiceField(queryset=Video.objects.filter(creado_por=perfil.entidad.id))
		form.fields['documentos']  = forms.ModelMultipleChoiceField(queryset=Documento.objects.filter(creado_por=perfil.entidad.id))
		ctx = {
			'form':form,
			'informacion':info,
			'blog':blog,
		}
		return render(request,'adminEntidad/entrada.html',ctx)
	else:
		return HttpResponseRedirect('/')


@login_required(login_url=LOGIN_URL)
def adminentidad_moderar_comentarios_blog_view(request):
	perfil = getPerfil(request.user)
	if perfil.tipo.id == 3:
		commentsSetForm = modelformset_factory(Comentario,form=ComentarioForm,extra=0)
		if request.method == 'POST':
			form = commentsSetForm(request.POST, request.FILES)
			if form.is_valid():
				for f in form:
					f.save()
		else:
			#Carga de datos para inicializacion del form
			blogs = Blog.objects.filter(entidad=perfil.entidad.id)
			ids_comentarios = []
			for blog in blogs:
				entradas = blog.entradas.all()
				for e in entradas:
					comentariosEntrada = e.comentarios.all()
					for c in comentariosEntrada:
						if c.estado.id == 1: #Comentario nuevo
							ids_comentarios += [c.id]
			form = commentsSetForm(queryset=Comentario.objects.filter(pk__in=ids_comentarios))
		ctx = {
			'form': form,
		}
		#pdb.set_trace()
		return render(request,'adminEntidad/comentarios.html',ctx)
	else:
		return HttpResponseRedirect('/')