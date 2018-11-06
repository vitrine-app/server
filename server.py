from flask import Flask
from flask_restful import Api

from models.game import Game

app = Flask(__name__)
api = Api(app)

api.add_resource(Game, '/games/<int:game_id>', endpoint='games')

if __name__ == '__main__':
    app.run(port=8000)
