from .base import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')#깃을 통해 올리므로 공개되면 안되기 때문에 env 파일에 따로 저장

DEBUG = True

ALLOWED_HOSTS = []