from programas.models import Programa
from userprofiles.models import UserProfile
from blogs.models import Blog

def myProcessor(request):
	producciones = Programa.objects.filter(produccion=True)
	blogs = Blog.objects.filter()
	currentUser = request.user
	if currentUser.is_authenticated():
		perfil = UserProfile.objects.get(user=currentUser)
	else:
		perfil = UserProfile()
	ctx = {
		"blogs":blogs,
		"producciones":producciones,
		"perfil":perfil,
	}
	return ctx