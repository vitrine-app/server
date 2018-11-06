from flask_restful import Resource


class Game(Resource):
    def __init__(self):
        super(Game, self).__init__()

    def get(self, game_id):
        return game_id
