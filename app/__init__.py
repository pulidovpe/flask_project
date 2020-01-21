from flask import Flask

app = Flask(__name__)

from .views import page

def create_app(config):
	app.config.from_object(config)	## Reiniciar servidor
	app.register_blueprint(page)
	return app