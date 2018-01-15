import os

#default config
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = '\x99\x83J2\xc4\xe0\xadc\x06\xf4\xd3%\x7f\xb3[\xaf\x87\xd1=\xb8\xb2a\xb3\xb9'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False