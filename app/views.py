from flask import Blueprint
from flask import render_template, request, flash, redirect, url_for

from flask_login import login_user, logout_user, login_required, current_user

from .models import User, Task
from .forms import LoginForm, RegisterForm, TaskForm
from .consts import *

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
		if user:
			if user.verify_password(form.password.data):
				login_user(user)
				flash(LOGIN)
				return redirect(url_for('.tasks'))
			else:
				flash(ERROR_PASSWORD, 'error')
		else:
			flash(ERROR_USER, 'error')

	return render_template('auth/login.html', title='Login', form=form)

@page.route('/logout')
def logout():
	logout_user()
	flash(LOGOUT)
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
			flash(USER_CREATED)
			return redirect(url_for('.tasks'))

	return render_template('auth/register.html', title='Registro', form=form)

@page.route('/tasks')
@login_required
def tasks():
	tasks = current_user.tasks
	return render_template('task/list.html', title='Tareas', tasks=tasks)

@page.route('/tasks/new', methods=['GET', 'POST'])
@login_required
def new_task():
	form = TaskForm(request.form)

	if request.method == 'POST' and form.validate():
		task = Task.create_element(form.title.data,form.description.data,current_user.id)
		if task:
			flash(TASK_CREATED)
			return redirect(url_for('.tasks'))

	return render_template('task/new.html', title='Nueva Tarea', form=form)