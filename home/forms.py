# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from userprofiles.models import UserProfile
from entidades.models import Entidad
from django.forms.extras.widgets import SelectDateWidget
from datetime import date

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))

class RegisterForm(forms.Form):
	username = forms.CharField(label="Nombre de Usuario",widget=forms.TextInput())
	email    = forms.EmailField(label="Correo Electronico",widget=forms.TextInput())
	password_one = forms.CharField(label="Contraseña",widget=forms.PasswordInput(render_value=False))
	password_two = forms.CharField(label="Confirmar contraseña",widget=forms.PasswordInput(render_value=False))

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('El nombre de usuario ya existe')

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('El email ya aparece registrado')

	def clean_password_two(self):
		password_one = self.cleaned_data['password_one']
		password_two = self.cleaned_data['password_two']
		if password_one == password_two:
			pass
		else:
			raise forms.ValidationError('las contraseñas no coinciden')

class ProfileForm(forms.Form):
	GENEROS = (
		('M', 'Masculino'),
		('F', 'Femenino'),
	)
	today = int(date.today().year)
	BIRTH_YEAR_CHOICES = (
		[i for i in reversed(range(1900,today))]
	)
	avatar = forms.ImageField(required=False)
	nombre = forms.CharField(widget = forms.TextInput(),required=False)
	apellidos = forms.CharField(widget = forms.TextInput(),required=False)
	email = forms.EmailField(widget = forms.TextInput(),required=False)
	sexo =  forms.ChoiceField(choices=GENEROS,required=False)
	entidad = forms.ModelChoiceField(queryset = Entidad.objects.all(),required=False)
	ciudad = forms.CharField(widget = forms.TextInput(),required=False)	
	fecha_nacimiento = forms.DateField(widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES),required=False)
	biografia = forms.CharField(widget = forms.Textarea(attrs={'rows':4, 'cols':60}),required=False)

	def clean(self):
		return self.cleaned_data

	def clean_image(self):
		avatar = self.cleaned_data.get('avatar',False)
		if avatar:
			if avatar._size > 1*1024*1024:
				raise ValidationError("avatar file too large ( > 1mb )")
			return avatar
		else:
			raise ValidationError("Couldn't read uploaded avatar")

class EmailForm(forms.Form):
	email = forms.EmailField(widget = forms.TextInput())

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			raise forms.ValidationError('El email no aparece registrado')	
		return email
		

class ChangePasswordForm(forms.Form):
	password_one = forms.CharField(label="Contraseña",widget=forms.PasswordInput(render_value=False))
	password_two = forms.CharField(label="Confirmar contraseña",widget=forms.PasswordInput(render_value=False))

	def clean_password_two(self):
		password_one = self.cleaned_data['password_one']
		password_two = self.cleaned_data['password_two']
		if password_one == password_two:
			pass
		else:
			raise forms.ValidationError('las contraseñas no coinciden')