import json
import os
from flask_restful import Resource

from lib_wrapper import lib, GoString


class Game(Resource):
    def __init__(self):
        super(Game, self).__init__()
        raw_key = os.getenv('IGDB_KEY')
        self.key = GoString(str.encode(raw_key), len(raw_key))

    def get(self, game_id):
        res = lib.GetGame(game_id, self.key)
        return {"result": json.loads(res.decode('utf-8'))}
