from wtforms import Form
from wtforms import StringField, PasswordField, validators, BooleanField, TextAreaField
from wtforms.fields.html5 import EmailField

from .models import User

def sysadmin_restriction(form, field):
	if field.data == 'sysadmin' or field.data == 'SYSADMIN' or field.data == 'Sysadmin':
		raise validators.ValidationError('Ese username no esta permitido!')

class LoginForm(Form):
	username = StringField('Username', [validators.Length(min=4, max=25, message='Username fuera de rango')])
	password = PasswordField('Password', [
        validators.DataRequired()])

class RegisterForm(Form):
	username = StringField('Username', [
		validators.length(min=4, max=50),
		sysadmin_restriction
	])
	email = EmailField('E-mail', [
		validators.length(min=6, max=100),
		validators.Required(message='El email es requerido'),
		validators.Email(message='Ingrese un email válido')
	])
	password = PasswordField('Password', [
		validators.Required('El password es requerido'),
		validators.EqualTo('confirm_password', message='La contraseña no coincide')
	])
	confirm_password = PasswordField('Confirme password')
	accept = BooleanField('', [
		validators.DataRequired()
	])

	def validate_username(self, username): 	## validate_NOMBREDELCAMPO
		if User.get_by_username(username.data):
			raise validators.ValidationError('El username ya se encuentra en uso!')

	def validate_email(self, email): 	## validate_NOMBREDELCAMPO
		if User.get_by_email(email.data):
			raise validators.ValidationError('El email ya se encuentra en uso!')

	def validate(self):
		if not Form.validate(self):  	## Recomendable primero las demas validaciones
			return False

		if len(self.password.data) < 3:
			self.password.errors.append('El password es demasiado corto!')
			return False

		return True  	## Obligatorio retornar un booleano

class TaskForm(Form):
	title = StringField('Título', [
		validators.Length(min=4, max=50, message='Título fuera de rango'),
		validators.DataRequired(message='El título es requerido')
	])
	description = TextAreaField('Descripción', [
		validators.DataRequired(message='La Descripción es requerida')
	], render_kw={'rows': 5})

