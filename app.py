from sanic import Sanic
from sanic.response import json
from sanic.views import HTTPMethodView
from sanic_jwt import exceptions
from sanic_jwt import initialize
from sanic_jwt import protected

from api import api

from auth import authenticate, retrieve_user

current_api_version = 1
app = Sanic(__file__)

app.blueprint(api, version=current_api_version)

initialize(app, authenticate=authenticate,
           retrieve_user=retrieve_user, url_prefix=f'/v{current_api_version}/api/auth')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8888)
