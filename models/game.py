import json
import os
from flask_restful import Resource

from games_catcher import games_catcher, GoString
from middlewares.auth import auth_middleware


class ApiGame(Resource):
    # method_decorators = [auth_middleware]

    def __init__(self):
        super(ApiGame, self).__init__()
        raw_key = os.getenv('IGDB_KEY')
        self.key = GoString(str.encode(raw_key), len(raw_key))

    def get(self, game_id):
        res = games_catcher.GetGame(game_id, self.key)
        return {"result": json.loads(res.decode('utf-8'))}
