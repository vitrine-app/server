from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from os import getenv

from models.game import ApiGame
from models.research import ApiResearch

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:' + getenv('MYSQL_ROOT_PASSWORD') + '@' + getenv('MYSQL_HOST') + '/vitrine'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
db = SQLAlchemy(app)

api.add_resource(ApiGame, '/games/<int:game_id>')
api.add_resource(ApiResearch, '/games/research/<string:game_name>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
