from programas.models import Programa
from userprofiles.models import UserProfile
from categorias.models import Categoria
from blogs.models import Blog
from fondos.models import Fondo

def myProcessor(request):
	fondoPrincipal = Fondo.objects.get(id=1)
	categorias = Categoria.objects.filter()
	producciones = Programa.objects.filter(produccion=True)
	blogs = Blog.objects.filter()
	currentUser = request.user
	if currentUser.is_authenticated():
		perfil = UserProfile.objects.get(user=currentUser)
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