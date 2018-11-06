import json
from flask_restful import Resource

from lib_wrapper import lib


class Game(Resource):
    def __init__(self):
        super(Game, self).__init__()

    def get(self, game_id):
        res = lib.get_game(game_id)
        return {"result": json.loads(res.decode('utf-8'))}
