class Config:
	SECRET_KEY = 'llavesecreta'

class DevelopmentConfig(Config):
	DEBUG = True
	## Reiniciar servidor

config = {
	'development': DevelopmentConfig,
	'default': DevelopmentConfig
}