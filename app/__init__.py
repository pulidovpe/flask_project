from flask import Flask

app = Flask(__name__)

from .views import page

def create_app():
	app.register_blueprint(page)
	
	return app