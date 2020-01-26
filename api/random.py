from sanic import Blueprint
from sanic.response import json
from sanic_jwt import protected, inject_user
from sanic_validation import validate_json

import random

from schema import random_schema


rnd = Blueprint('random', url_prefix='/random')

@rnd.route('/', methods=['GET'], version=1)
async def get_random(request):
    return json({'random': random.random()})

@rnd.route('/', methods=['POST'], version=1)
@inject_user()
@protected()
@validate_json(random_schema, clean=True)
async def get_random_with_state(request, user, valid_json):
    random.seed(valid_json['state'])
    return json({'random': random.random(), 'user': user.to_dict()})
