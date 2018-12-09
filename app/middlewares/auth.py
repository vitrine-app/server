import jwt
from functools import wraps
from flask_restful import abort, reqparse
from os import getenv
from time import time

request_delay = 5


def auth_middleware(func):
    @wraps(func)
    def func_wrapper(*args, **kwargs):
        parser = reqparse.RequestParser()
        parser.add_argument('Authorization', location='headers')
        try:
            token = parser.parse_args().__getattr__('Authorization')
            decoded = jwt.decode(token, getenv('VITRINE_PRIVATE_KEY'))
            request_timestamp = int(decoded.get('date') / 1000)
            current_timestamp = int(time())
            if current_timestamp - request_timestamp > request_delay:
                raise Exception('Request took too long to proceed.')
        except Exception as e:
            abort(401, description=str(e))
        return func(*args, **kwargs)

    return func_wrapper
