from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from os import getenv

from app.models.game import Game as ApiGame
from app.models.first_game import FirstGame as ApiFirstGame
from app.models.research import Research as ApiResearch

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:' + getenv('MYSQL_ROOT_PASSWORD') + '@' + getenv('MYSQL_HOST') + '/vitrine'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
db = SQLAlchemy(app)

api.add_resource(ApiGame, '/games/<int:game_id>')
api.add_resource(ApiFirstGame, '/games/research/<string:game_name>')
api.add_resource(ApiResearch, '/games/research/<string:game_name>/<int:list_size>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
