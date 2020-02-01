class Config:
	SECRET_KEY = 'llavesecreta'

class DevelopmentConfig(Config):
	DEBUG = True 	## Reiniciar servidor
	SQLALCHEMY_DATABASE_URI = 'mysql://developer:123456@localhost/bd_project_web_facilito'

config = {
	'development': DevelopmentConfig,
	'default': DevelopmentConfig
}