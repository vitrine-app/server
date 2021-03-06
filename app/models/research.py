import json
from flask_restful import Resource

from games_catcher import games_catcher, GoString
from app.middlewares.auth import auth_middleware


class Research(Resource):
    method_decorators = [auth_middleware]

    def get(self, game_name, list_size):
        res = games_catcher.ResearchGames(GoString(str.encode(game_name), len(game_name)), list_size)
        return {"data": json.loads(res.decode('utf-8'))}
