# -*- encoding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from informacion_canal.models import InfoCanal
from documentos_en_linea.models import DocumentoEnLinea
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from home.forms import LoginForm
from home.forms import RegisterForm
from home.forms import ProfileForm
from home.forms import EmailForm
from home.forms import ChangePasswordForm
from django.contrib.auth.models import User
from userprofiles.models import UserProfile
from tipos_usuario.models import TipoUsuario
from django.core.exceptions import ObjectDoesNotExist
from carrusel.models import Carrusel
from noticias_destacadas.models import NoticiasDestacadas
from videos.models import Video
from datetime import date
from programaciones.models import Programacion
from horarios_programacion.models import HorarioProgramacion
from franjas.models import Franja
from datetime import datetime
from oportunidades.models import Oportunidad
from eventos.models import Evento
from entidades.models import Entidad
from encuestas.models import Encuesta
from django.core.mail import EmailMultiAlternatives
from paginas.models import Pagina
from imagenes.models import Imagen
from entradas_blogs.models import EntradaBlog
from noticias.models import Noticia
from programas.models import Programa
from respuestas_encuestas.models import RespuestaEncuesta
from suscriptores.models import Suscriptor
from datetime import datetime 
from django.utils import timezone
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage

import time, hashlib, random
#import twitter

import pdb

def index_view(request, mensaje=None):

	if request.method == "GET":
		if "mensaje" in request.GET:
			mensaje = request.GET['mensaje']

	#Carrusel
	carrusel = get_object_or_404(Carrusel, id=1)
	noticiasDestacadas = get_object_or_404(NoticiasDestacadas, id=1)
	pagina = Pagina.objects.get(id=1)
	numeroItems = carrusel.noticias.count() + carrusel.oportunidades.count() + carrusel.eventos.count() + carrusel.entradas.count()
	items = [] # array utilizado para el despliegue de controles del carrusel
	for i in range(numeroItems):
		items.append(i)

	#Videos
	videos = Video.objects.order_by("-id")[:12]

	#Programacion
	programacionDia = getProgramacionDia(date.today())
	horaActual = datetime.now().time()
	horariosProgramacion = HorarioProgramacion.objects.filter().order_by('manana')
	id_horario = 1
	for horario in horariosProgramacion:
		if horaActual > horario.manana:
			id_horario = horario.id
			esHorarioManana = True
	for horario in horariosProgramacion:
		if horaActual > horario.tarde_noche:
			id_horario = horario.id
			esHorarioManana = False

	eventos = Evento.objects.filter(fin__gte=timezone.now()).order_by("inicio")[:4]
	aliados = Entidad.objects.filter(tipo__id=3,activo=True)
	iesAfiliadas = Entidad.objects.filter(tipo__id=2,activo=True)
	encuestas = Encuesta.objects.filter(activa=True)[:1]
	encuesta = encuestas[0]

	totalVotos = 0
	for respuesta in encuesta.respuestas.all():
		totalVotos += respuesta.votos

	porcentajes = []
	for respuesta in encuesta.respuestas.all():
		if totalVotos == 0:
			value = 0
		else:
			value = ( respuesta.votos * 100 ) / totalVotos
		porcentajes.append(value)

	resultados = zip(encuesta.respuestas.all(), porcentajes)

	horarioProgramacionActual = HorarioProgramacion.objects.get(id=id_horario)

	yaVoto = ""
	if "yaVoto" in request.session:
		yaVoto = request.session["yaVoto"]
	else:
		request.session["yaVoto"] = "False"

	filters = Q()
	filters = filters & Q(categorias__id__in = [6])
	noticiasEfemerides = Noticia.objects.filter(filters).order_by("-id")[:6]

	ctx = {
		'items':items,
		'carrusel':carrusel,
		'videos':videos,
		'programacionDia':programacionDia,
		'horarioProgramacionActual':horarioProgramacionActual,
		'esHorarioManana':esHorarioManana,
		'eventos':eventos,
		'aliados':aliados,
		'pagina':pagina,
		'noticiasDestacadas':noticiasDestacadas,
		'encuesta':encuesta,
		'resultados':resultados,
		'yaVoto':yaVoto,
		'noticiasEfemerides':noticiasEfemerides,
		'iesAfiliadas':iesAfiliadas,
		'mensaje':mensaje,		
	}
	#pdb.set_trace()
	return render(request, 'home/index.html',ctx)

def senal_en_vivo_view(request):
	pagina = Pagina.objects.get(id=22)
	ctx = {
		'pagina':pagina,
	}
	return render(request, 'home/senalenvivo.html',ctx)

def acerca_de_zoom_view(request):
	pagina = Pagina.objects.get(id=2)
	info = get_object_or_404(InfoCanal, id=1)
	titulo = "Acerca de Canal ZOOM"
	descripcion = "Información acerca de Canal ZOOM"
	info.acerca_de_zoom = "<br>".join(info.acerca_de_zoom.split("\n"))
	ctx = {
		'titulo':titulo,
		'descripcion':descripcion,
		'info':info.acerca_de_zoom,
		'imagen':info.imagen_acerca_de_zoom,
		'pagina':pagina,
	}
	return render(request, 'home/info.html', ctx)

def equipo_zoom_view(request):
	pagina = Pagina.objects.get(id=2)
	info = get_object_or_404(InfoCanal, id=1)
	titulo = "Equipo de trabajo"
	descripcion = "Equipo de trabajo Canal ZOOM"
	info.equipo_de_trabajo = "<br>".join(info.equipo_de_trabajo.split("\n"))
	ctx = {
		'titulo':titulo,
		'descripcion':descripcion,
		'info':info.equipo_de_trabajo,
		'imagen':info.imagen_equipo_de_trabajo,
		'imagenes_adicionales': info.imagenes_adicionales_equipo_de_trabajo,
		'pagina':pagina,
	}
	return render(request, 'home/info.html', ctx)

def comite_programacion_view(request):
	pagina = Pagina.objects.get(id=2)
	info = get_object_or_404(InfoCanal, id=1)
	titulo = "Comité de Programación"
	descripcion = "Comité de Programación Canal ZOOM"
	info.comite_de_programacion = "<br>".join(info.comite_de_programacion.split("\n"))
	ctx = {
		'titulo':titulo,
		'descripcion':descripcion,
		'info':info.comite_de_programacion,
		'pagina':pagina,
	}
	return render(request, 'home/info.html', ctx)
	
def comites_tecnicos_regionales_view(request):
	pagina = Pagina.objects.get(id=2)
	info = get_object_or_404(InfoCanal, id=1)
	titulo = "Comités Regionales"
	descripcion = "Comités regionales Canal ZOOM"
	info.comites_tecnicos_regionales = "<br>".join(info.comites_tecnicos_regionales.split("\n"))
	ctx = {
		'titulo':titulo,
		'descripcion':descripcion,
		'info':info.comites_tecnicos_regionales,
		'pagina':pagina,
	}
	return render(request, 'home/info.html', ctx)

def documentos_view(request):
	pagina = Pagina.objects.get(id=2)
	info = get_object_or_404(InfoCanal, id=1)
	titulo = "Documentos"
	descripcion = "Documentos Canal ZOOM"
	documentosEnLinea = DocumentoEnLinea.objects.filter()
	ctx = {
		'titulo':titulo,
		'descripcion':descripcion,
		'documentos':info.documentos,
		'documentosEnLinea':documentosEnLinea,
		'pagina':pagina,
	}
	return render(request, 'home/info.html', ctx)

def login_view(request):
	pagina = Pagina.objects.get(id=12)
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method== "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				usuario = authenticate(username=username,password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect('/')
				else:
					mensaje = "El usuario y/o password es incorrecto o tu cuenta no esta activa."
		form = LoginForm()
		ctx = {
			'form':form,
			'mensaje':mensaje,
			'pagina':pagina,
		}
		return render(request,'home/login.html',ctx)

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def registro_view(request):
	pagina = Pagina.objects.get(id=13)
	form = RegisterForm()
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			usuario = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password_one = form.cleaned_data['password_one']
			password_two = form.cleaned_data['password_two']
			u = User.objects.create_user(username=usuario,email=email,password=password_one)
			u.is_active = False
			u.save() # Guardar el usuario

			salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
			activation_key = hashlib.sha1(salt+email).hexdigest()
			t = TipoUsuario.objects.get(id=2)
			up = UserProfile.objects.create(user=u,tipo=t, activation_key=activation_key)
			up.anotaciones_internas = "Creacion de usuario (" + str(datetime.now()) +")\n"
			up.save()
			# Envio de mensaje via email
			to = email
			html_content = "<img src='http://kamaylab.com/zoomcanal/img/logozoom.jpg'><br><br>Gracias por registrarte en el Sitio Web de Canal ZOOM<br><br><br>Para activar tu cuenta da click en el siquiente link.<br><br>http://127.0.0.1:8000/confirm/%s" %(activation_key)
			msg =EmailMultiAlternatives('Confirma tu email en Canal ZOOM',html_content,'administrador@zoomcanal.com.co',[to])
			msg.attach_alternative(html_content,'text/html') #Define el contenido como HTML
			msg.send()
			return HttpResponseRedirect('/login/')
		else:
			ctx = {
				'form':form,
				'pagina':pagina,
			}
			return  render(request,'home/registro.html',ctx)
	ctx = {
		'form':form,
		'pagina':pagina,
	}
	return render(request,'home/registro.html',ctx)


def perfil_view(request):
	pagina = Pagina.objects.get(id=19)
	if request.user.is_authenticated():
		user = request.user
		imagenAvatar = ""
		try:
			perfil = UserProfile.objects.get(user=user)
			form = ProfileForm()
		except ObjectDoesNotExist:
			t = TipoUsuario.objects.get(id=2)
			perfil = UserProfile.objects.create(user=user,tipo=t)
			perfil.save()
			form = ProfileForm(instance=perfil)

		if request.method == "POST":
			form = ProfileForm(request.POST,request.FILES)
			if form.is_valid():
				user.first_name = form.cleaned_data['nombre']
				user.last_name = form.cleaned_data['apellidos']
				user.email = form.cleaned_data['email']
				user.save()

				perfil.biografia = form.cleaned_data['biografia']
				perfil.ciudad = form.cleaned_data['ciudad']
				perfil.sexo = form.cleaned_data['sexo']
				perfil.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
				if form.cleaned_data['avatar']:
					perfil.avatar = form.cleaned_data['avatar']
				perfil.entidad = form.cleaned_data['entidad']
				perfil.save()
				imagenAvatar = perfil.avatar.name
				info = "Se guardo satisfactoriamente"
				#pdb.set_trace()
		else:
			default_data = {
			'nombre': user.first_name,
			'apellidos': user.last_name,
			'email': user.email,
			'biografia': perfil.biografia,
			'ciudad': perfil.ciudad,
			'sexo': perfil.sexo,
			'fecha_nacimiento': perfil.fecha_nacimiento,
			'avatar': perfil.avatar,
			'entidad': perfil.entidad,
			}
			form = ProfileForm(default_data, auto_id=False)
			imagenAvatar = perfil.avatar.name
		ctx = {
			'form':form,
			'imagenAvatar':imagenAvatar,
			'pagina':pagina,
		}
		return render(request,'home/perfil.html',ctx)

	else:
		return HttpResponseRedirect('/login/')

def verperfil_view(request,id_perfil):
	pagina = Pagina.objects.get(id=19)
	try:
		perfil = UserProfile.objects.get(id=id_perfil)
		perfil.biografia = "<br>".join(perfil.biografia.split("\n"))
	except ObjectDoesNotExist:
		return HttpResponseRedirect('/')
	ctx = {
		'perfil':perfil,
	}
	return render(request,'home/verperfil.html',ctx)

def getProgramacionDia(fechaDia):
	horariosProgramacion = HorarioProgramacion.objects.filter().order_by('manana')

	#Trae la programacion del dia (puede traer horas sin programas)
	programacionDia = Programacion.objects.filter(fecha=fechaDia)

	# se trae el listado de horas con programacion
	horasProgramadasDia = Programacion.objects.filter(fecha=fechaDia).values_list('horario__manana',flat=True)

	# Se completa la programacion del dia incluyendo programas vacios para un renderizado correcto
	sinFranjaAsignada = Franja.objects.get(nombre="Sin Franja Asignada")
	programacionCompletaDia = []
	for horario in horariosProgramacion:
		if horario.manana in horasProgramadasDia:
			programa = programacionDia.get(horario=horario)
			programa.programa = programa.programa + "\nFranja: " + programa.franja.nombre
		else:
			programa = Programacion(fecha=fechaDia, horario=horario, programa="",franja=sinFranjaAsignada)
		programacionCompletaDia.append(programa)			
	return programacionCompletaDia

def register_confirm_view(request, activation_key):
	if request.user.is_authenticated():
		HttpResponseRedirect('/')
	user_profile = get_object_or_404(UserProfile, activation_key=activation_key)
	user = user_profile.user
	user.is_active = True
	user.save()
	user_profile.anotaciones_internas = user_profile.anotaciones_internas + "Confirmacion inicial email (" + str(datetime.now()) +")\n"
	user_profile.save()
	return HttpResponseRedirect('/login/')

def ask_email_view(request):
	form = EmailForm()
	if request.method == "POST":
		form = EmailForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			user = User.objects.get(email=email)
			try:
				perfil = UserProfile.objects.get(user=user)
			except ObjectDoesNotExist:
				t = TipoUsuario.objects.get(id=2)
				perfil = UserProfile.objects.create(user=user,tipo=t)
				perfil.save()
			salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
			activation_key = hashlib.sha1(salt+email).hexdigest()
			perfil.activation_key = activation_key
			perfil.save()
			to = email
			html_content = "<img src='http://kamaylab.com/zoomcanal/img/logozoom.jpg'><br><br>Sitio Web de Canal ZOOM<br><br><br>Tu nombre de usuario es: <strong>%s</strong><br><br><br>Para cambiar tu contrase&ntilde;a da click en el siquiente link.<br><br>http://127.0.0.1:8000/cambiar_contrasena/%s" %(user.username,activation_key)
			msg =EmailMultiAlternatives('Cambio de contraseña en Canal ZOOM',html_content,'administrador@zoomcanal.com.co',[to])
			msg.attach_alternative(html_content,'text/html') #Define el contenido como HTML
			msg.send()
			return HttpResponseRedirect('/login/')
	ctx = {'form':form}
	return render(request,'home/email.html',ctx)


def change_password_view(request, activation_key):
	form = ChangePasswordForm()
	if request.method == "POST":
		form = ChangePasswordForm(request.POST)
		if form.is_valid():
			user_profile = get_object_or_404(UserProfile, activation_key=activation_key)
			user = user_profile.user
			user.set_password(form.cleaned_data['password_one'])
			user.save()
			user_profile.anotaciones_internas = user_profile.anotaciones_internas + "Cambio de contrasena (" + str(datetime.now()) +")\n"
			user_profile.save()
			return HttpResponseRedirect('/login/')
	ctx = {'form':form}
	return render(request,'home/nueva_contrasena.html',ctx)

def lista_fees_view(request):
	return render(request,'home/feeds.html')	

def responder_encuesta_view(request):
	if request.method == "POST":
		if "encuestaId" in request.POST:
			encuestaId = request.POST['encuestaId']
			respuestaId = request.POST['respuesta']
			respuestaEncuesta = RespuestaEncuesta.objects.get(id=respuestaId)
			respuestaEncuesta.votos += 1
			respuestaEncuesta.save()
			request.session["yaVoto"] = "True"
	return HttpResponseRedirect('/')

def new_suscriptor_view(request):
	if request.method == "POST":
		if "email" in request.POST:
			Suscriptor.objects.get_or_create(email=request.POST['email'])
			return HttpResponseRedirect('/?mensaje=Gracias por suscribirte a nuestro boletín. Dentro de poco lo recibiras en tu email.')
	return HttpResponseRedirect('/')

def busqueda_view(request,id_pagina=1):
	pagina = Pagina.objects.get(id=25)
	paginas = []
	listaItems = []
	numeroTotalItems = 0
	listaItemsPorPagina = []
	palabrasABuscar = None

	if request.method == "POST":
		if "palabras" in request.POST:
			request.session["palabrasABuscar"] = request.POST['palabras']
	else:
		if not "palabrasABuscar" in request.session:
			request.session["palabrasABuscar"] = ""
	palabrasABuscar = request.session["palabrasABuscar"].split()

	if len(palabrasABuscar) > 0:
		# Busqueda de noticias
		filters = Q()
		filters = filters | (reduce(lambda x, y: x & y, [Q(titulo__icontains=palabra) for palabra in palabrasABuscar]))
		filters = filters | (reduce(lambda x, y: x & y, [Q(lead__icontains=palabra) for palabra in palabrasABuscar]))
		filters = filters | (reduce(lambda x, y: x & y, [Q(contenido__icontains=palabra) for palabra in palabrasABuscar]))
		listaTemporal = Noticia.objects.filter(filters).order_by("-id")
		for item in listaTemporal:
			info = {}
			info['tipo'] = "Noticia"
			info['link'] = "/noticias/" + str(item.id) + "/"
			info['titulo'] = item.titulo
			info['descripcion'] = item.lead + " " + item.contenido
			listaItems.append(info)
			numeroTotalItems += 1

		# Busqueda de oportunidades
		filters = Q()
		filters = filters | (reduce(lambda x, y: x & y, [Q(nombre__icontains=palabra) for palabra in palabrasABuscar]))
		filters = filters | (reduce(lambda x, y: x & y, [Q(descripcion__icontains=palabra) for palabra in palabrasABuscar]))
		listaTemporal = Oportunidad.objects.filter(filters).order_by("-id")
		for item in listaTemporal:
			info = {}
			info['tipo'] = "Oportunidad"
			info['link'] = "/oportunidades/" + str(item.id) + "/"
			info['titulo'] = item.nombre
			info['descripcion'] = item.descripcion
			listaItems.append(info)
			numeroTotalItems += 1

		# Busqueda de eventos
		filters = Q()
		filters = filters | (reduce(lambda x, y: x & y, [Q(nombre__icontains=palabra) for palabra in palabrasABuscar]))
		filters = filters | (reduce(lambda x, y: x & y, [Q(descripcion__icontains=palabra) for palabra in palabrasABuscar]))
		listaTemporal = Evento.objects.filter(filters).order_by("-id")
		for item in listaTemporal:
			info = {}
			info['tipo'] = "Evento"
			info['link'] = "/eventos/" + str(item.id) + "/"
			info['titulo'] = item.nombre
			info['descripcion'] = item.descripcion
			listaItems.append(info)
			numeroTotalItems += 1

		# Busqueda de blogs
		filters = Q()
		filters = filters | (reduce(lambda x, y: x & y, [Q(titulo__icontains=palabra) for palabra in palabrasABuscar]))
		filters = filters | (reduce(lambda x, y: x & y, [Q(lead__icontains=palabra) for palabra in palabrasABuscar]))
		filters = filters | (reduce(lambda x, y: x & y, [Q(contenido__icontains=palabra) for palabra in palabrasABuscar]))
		listaTemporal = EntradaBlog.objects.filter(filters).order_by("-id")
		for item in listaTemporal:
			info = {}
			info['tipo'] = "Entrada Blog"
			info['link'] = "/blogs/entradas/" + str(item.id) + "/"
			info['titulo'] = item.titulo
			info['descripcion'] = item.lead + " " + item.contenido
			listaItems.append(info)
			numeroTotalItems += 1

		# Busqueda de producciones
		filters = Q()
		filters = filters | (reduce(lambda x, y: x & y, [Q(nombre__icontains=palabra) for palabra in palabrasABuscar]))
		filters = filters | (reduce(lambda x, y: x & y, [Q(sinopsis__icontains=palabra) for palabra in palabrasABuscar]))
		listaTemporal = Programa.objects.filter(filters).order_by("-id")
		for item in listaTemporal:
			info = {}
			info['tipo'] = "Produccion"
			info['link'] = "/producciones/" + str(item.id) + "/"
			info['titulo'] = item.nombre
			info['descripcion'] = item.sinopsis
			listaItems.append(info)
			numeroTotalItems += 1

		# Busqueda de videos
		filters = Q()
		filters = filters | (reduce(lambda x, y: x & y, [Q(nombre__icontains=palabra) for palabra in palabrasABuscar]))
		filters = filters | (reduce(lambda x, y: x & y, [Q(descripcion__icontains=palabra) for palabra in palabrasABuscar]))
		listaTemporal = Video.objects.filter(filters).order_by("-id")
		for item in listaTemporal:
			info = {}
			info['tipo'] = "Video"
			info['link'] = "/videos/" + str(item.id) + "/"
			info['titulo'] = item.nombre
			info['descripcion'] = item.descripcion
			listaItems.append(info)
			numeroTotalItems += 1

		# Busqueda de imagenes
		filters = Q()
		filters = filters | (reduce(lambda x, y: x & y, [Q(nombre__icontains=palabra) for palabra in palabrasABuscar]))
		filters = filters | (reduce(lambda x, y: x & y, [Q(descripcion__icontains=palabra) for palabra in palabrasABuscar]))
		listaTemporal = Imagen.objects.filter(filters).order_by("-id")
		for item in listaTemporal:
			info = {}
			info['tipo'] = "Imagen"
			info['link'] = "/imagenes/" + str(item.id) + "/"
			info['titulo'] = item.nombre
			info['descripcion'] = item.descripcion
			listaItems.append(info)
			numeroTotalItems += 1

		numeroTotalItems = len(listaItems)
		paginator = Paginator(listaItems, 10) #Cuantos items van por pagina

		for numPagina in range(paginator.num_pages):
			paginas += [str(numPagina+1)]

		try:
			page = int(id_pagina)
		except:
			page = 1
		try:
			listaItemsPorPagina = paginator.page(page)
		except (EmptyPage, InvalidPage):
			listaItemsPorPagina = paginator.page(paginator.num_pages)

	ctx = {
		'palabrasABuscar': " ".join(palabrasABuscar),
		'listaItems':listaItemsPorPagina,
		'numeroTotalItems':numeroTotalItems,
		'paginas':paginas,
		'pagina':pagina,
	}
	return render(request, 'home/busqueda.html',ctx)