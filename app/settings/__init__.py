import environ

root = environ.Path(__file__) - 1
env = environ.Env()
environ.Env.read_env()

environment = str(env('ENVIRONMENT')).lower()

if environment == 'production':
    from .production import *
else:
    from .local import *
