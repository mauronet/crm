from django import forms
from imagenes.models import Imagen
from videos.models import Video
from documentos.models import Documento
from programas.models import Programa
from capitulos.models import Capitulo
from entradas_blogs.models import EntradaBlog
from comentarios.models import Comentario
from estados_comentarios.models import EstadoComentario

class addImagenForm(forms.ModelForm):
	class Meta:
		model = Imagen
		exclude = {'creado_por'}

	def __init__(self, *args, **kwargs):
	    super(addImagenForm, self).__init__(*args, **kwargs)
	    self.fields['nombre'].widget.attrs = {'size': 60,}
	    self.fields['descripcion'].widget.attrs = {'rows':4, 'cols':60}
	    self.fields['creditos'].widget.attrs = {'rows':4, 'cols':60}


class addVideoForm(forms.ModelForm):
	class Meta:
		model = Video
		exclude = {'creado_por'}

	def __init__(self, *args, **kwargs):
	    super(addVideoForm, self).__init__(*args, **kwargs)
	    self.fields['nombre'].widget.attrs = {'size': 60,}
	    self.fields['descripcion'].widget.attrs = {'rows':4, 'cols':60}
	    self.fields['creditos'].widget.attrs = {'rows':4, 'cols':60}

class addDocumentoForm(forms.ModelForm):
	class Meta:
		model = Documento
		exclude = {'creado_por'}

	def __init__(self, *args, **kwargs):
	    super(addDocumentoForm, self).__init__(*args, **kwargs)
	    self.fields['nombre'].widget.attrs = {'size': 60,}
	    self.fields['descripcion'].widget.attrs = {'rows':4, 'cols':60}


class addProgramaForm(forms.ModelForm):
	class Meta:
		model = Programa
		exclude = {'franja','entidad','produccion','capitulos'}

	def __init__(self, *args, **kwargs):
	    super(addProgramaForm, self).__init__(*args, **kwargs)
	    self.fields['nombre'].widget.attrs = {'size': 60,}
	    self.fields['sinopsis'].widget.attrs = {'rows':4, 'cols':60}


class addCapituloForm(forms.ModelForm):
	class Meta:
		model = Capitulo

	def __init__(self, *args, **kwargs):
	    super(addCapituloForm, self).__init__(*args, **kwargs)
	    self.fields['nombre'].widget.attrs = {'size': 60,}
	    self.fields['descripcion'].widget.attrs = {'rows':4, 'cols':60}
	    self.fields['direccion'].widget.attrs = {'rows':4, 'cols':60}
	    self.fields['produccion'].widget.attrs = {'rows':4, 'cols':60}
	    self.fields['duracion'].widget.attrs = {'size': 60,}


class addEntradaBlogForm(forms.ModelForm):
	class Meta:
		model = EntradaBlog
		exclude = {'comentarios','fecha'}

	def __init__(self, *args, **kwargs):
	    super(addEntradaBlogForm, self).__init__(*args, **kwargs)
	    self.fields['titulo'].widget.attrs = {'size': 60,}
	    self.fields['lead'].widget.attrs = {'rows':4, 'cols':60}
	    self.fields['contenido'].widget.attrs = {'rows':4, 'cols':60}

class ComentarioForm(forms.ModelForm):
	class Meta:
		model = Comentario

	def __init__(self, *args, **kwargs):
		super(ComentarioForm, self).__init__(*args, **kwargs)
		self.fields['contenido'].widget.attrs = {'rows':4, 'cols':60, 'readonly':True}
		self.fields['fecha'].widget.attrs['readonly'] = True
		self.fields['usuario'].widget.attrs['readonly'] = True