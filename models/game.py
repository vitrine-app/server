import json
import os
from flask_restful import Resource

from lib_wrapper import lib


class Game(Resource):
    def __init__(self):
        super(Game, self).__init__()

    def get(self, game_id):
        res = lib.GetGame(game_id, os.getenv('IGDB_KEY'))
        return {"result": json.loads(res.decode('utf-8'))}
