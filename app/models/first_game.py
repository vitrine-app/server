import json
from flask_restful import Resource

from games_catcher import games_catcher, GoString
from app.middlewares.auth import auth_middleware


class FirstGame(Resource):
    method_decorators = [auth_middleware]

    def get(self, game_name):
        res = games_catcher.GetFirstGame(GoString(str.encode(game_name), len(game_name)))
        return {"data": json.loads(res.decode('utf-8'))}
