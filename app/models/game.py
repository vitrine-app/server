import json
from flask_restful import Resource

from games_catcher import games_catcher
from app.middlewares.auth import auth_middleware


class Game(Resource):
    method_decorators = [auth_middleware]

    def get(self, game_id):
        res = games_catcher.GetGame(game_id)
        return {"data": json.loads(res.decode('utf-8'))}
