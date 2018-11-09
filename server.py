from flask import Flask
from flask_restful import Api

from lib.keys import populate_keys
from models.game import Game

app = Flask(__name__)
api = Api(app)

api.add_resource(Game, '/games/<int:game_id>', endpoint='games')


if __name__ == '__main__':
    populate_keys()
    app.run(host='0.0.0.0', port=8000)
