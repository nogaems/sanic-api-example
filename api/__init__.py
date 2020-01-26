from sanic import Blueprint
from .random import rnd

api = Blueprint.group(rnd, url_prefix='/api')
