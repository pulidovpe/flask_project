class Config:
	SECRET_KEY = 'llavesecreta'

class DevelopmentConfig(Config):
	DEBUG = True 	## Reiniciar servidor
	
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/db_flask_project'

	SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
	'development': DevelopmentConfig,
	'default': DevelopmentConfig
}