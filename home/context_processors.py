from programas.models import Programa
from userprofiles.models import UserProfile
from categorias.models import Categoria
from blogs.models import Blog
from fondos.models import Fondo
from django.core.exceptions import ObjectDoesNotExist
from tipos_usuario.models import TipoUsuario
from django.conf import settings

def myProcessor(request):
	fondoPrincipal = Fondo.objects.get(id=1)
	categorias = Categoria.objects.filter()
	producciones = Programa.objects.filter(produccion=True)
	blogs = Blog.objects.filter()
	currentUser = request.user
	if currentUser.is_authenticated():
		try:
			perfil = UserProfile.objects.get(user=currentUser)
		except ObjectDoesNotExist:
			t = TipoUsuario.objects.get(id=2)
			perfil = UserProfile.objects.create(user=currentUser,tipo=t)
			perfil.save()
	else:
		perfil = UserProfile()
	ctx = {
		"fondoPrincipal":fondoPrincipal,
		"blogs":blogs,
		"producciones":producciones,
		"perfil":perfil,
		"categorias":categorias,
	}
	return ctx


def google_analytics(request):
	"""
	Use the variables returned in this function to
	render your Google Analytics tracking code template.
	"""
	ga_prop_id = getattr(settings, 'GOOGLE_ANALYTICS_PROPERTY_ID', False)
	ga_domain = getattr(settings, 'GOOGLE_ANALYTICS_DOMAIN', False)
	if not settings.DEBUG and ga_prop_id and ga_domain:
		return {
			'GOOGLE_ANALYTICS_PROPERTY_ID': ga_prop_id,
			'GOOGLE_ANALYTICS_DOMAIN': ga_domain,
		}
	return {}