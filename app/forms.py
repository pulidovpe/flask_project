from wtforms import Form
from wtforms import StringField, PasswordField, validators

class LoginForm(Form):
	username = StringField('Username', [validators.Length(min=4, max=25, message='Username fuera de rango')])
	password = PasswordField('Password', [
        validators.DataRequired()])