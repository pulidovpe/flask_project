class Config:
	pass

class DevelopmentConfig(Config):
	DEBUG = True
	## Reiniciar servidor

config = {
	'development': DevelopmentConfig,
	'default': DevelopmentConfig
}