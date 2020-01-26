from sanic import Sanic
from sanic.response import json
from sanic.views import HTTPMethodView
from sanic_jwt import exceptions
from sanic_jwt import initialize
from sanic_jwt import protected

from api import api

from auth import authenticate, retrieve_user

app = Sanic()

app.blueprint(api, version=1)

initialize(app, authenticate=authenticate, retrieve_user=retrieve_user)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8888)


