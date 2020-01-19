from flask import Blueprint

page = Blueprint('page', __name__)

@page.route('/')
def index():
	return 'Hola mundo'