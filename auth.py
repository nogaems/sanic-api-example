from sanic_jwt import exceptions
from db import username_table, userid_table

async def authenticate(request, *args, **kwargs):
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        raise exceptions.AuthenticationFailed('Missing username or password.')

    user = username_table.get(username, None)

    if not user:
        raise exceptions.AuthenticationFailed('User not found.')
    if password != user.password:
        raise exceptions.AuthenticationFailed('Password is incorrect.')

    return user

async def retrieve_user(request, payload, *args, **kwargs):
    user = userid_table.get(payload['user_id'])
    return user
