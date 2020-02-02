from flask import Blueprint
from flask import render_template, request, flash, redirect, url_for

from flask_login import login_user, logout_user, login_required, current_user

from .models import User
from .forms import LoginForm, RegisterForm

from . import login_manager

page = Blueprint('page', __name__)

@login_manager.user_loader
def load_user(id):
	return User.get_by_id(id)

@page.route('/')
def index():
	return render_template('index.html', title='Index')

@page.app_errorhandler(404)
def page_not_found(error):
	return render_template('errors/404.html'), 404

@page.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('.tasks'))

	form = LoginForm(request.form)

	if request.method == 'POST' and form.validate():
		user = User.get_by_username(form.username.data)
		##print(form.username.data)
		##print(form.password.data)
		if user:
			if user.verify_password(form.password.data):
				login_user(user)
				flash("Usuario autenticado exitosamente.")
				return redirect(url_for('.tasks'))
			else:
				flash("Password incorrecto.", 'error')
		else:
			flash("Usuario no existe.", 'error')

	return render_template('auth/login.html', title='Login', form=form)

@page.route('/logout')
def logout():
	logout_user()
	flash("Sesión cerrada exitosamente!")
	return redirect(url_for('.login'))


@page.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('.tasks'))

	form = RegisterForm(request.form)

	if request.method == 'POST':
		if form.validate():
			user = User.create_element(form.username.data, form.password.data, form.email.data)
			login_user(user)
			flash("Usuario registrado exitosamente!")
			return redirect(url_for('.tasks'))

	return render_template('auth/register.html', title='Registro', form=form)

@page.route('/tasks')
@login_required
def tasks():
	return render_template('task/list.html', title='Tareas')