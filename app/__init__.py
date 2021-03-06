from flask import Flask

from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()
csrf = CSRFProtect()
bootstrap = Bootstrap()
login_manager = LoginManager()

from .views import page
from .models import User

def create_app(config):
	app.config.from_object(config)	## Reiniciar servidor

	csrf.init_app(app)
	bootstrap.init_app(app)
	login_manager.init_app(app)
	login_manager.login_view = '.login'
	login_manager.login_message = 'Inicio de sesión requerido'
	
	app.register_blueprint(page)

	with app.app_context():
		db.init_app(app)
		db.create_all()

	return app