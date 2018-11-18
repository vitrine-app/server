import json
from flask_restful import Resource

from games_catcher import games_catcher, GoString
from middlewares.auth import auth_middleware


class ApiResearch(Resource):
    method_decorators = [auth_middleware]

    def get(self, game_name):
        print("ici pignouf omega")
        res = games_catcher.GetFirstGame(GoString(str.encode(game_name), len(game_name)))
        print(res.decode('utf-8'))
        return {"result": json.loads(res.decode('utf-8'))}
