from datetime import datetime
from os import getenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

db_uri = 'mysql://root:' + getenv('MYSQL_ROOT_PASSWORD') + '@' + getenv('MYSQL_HOST') + '/vitrine'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

games_genres = db.Table('games_genres',
                        db.Column('game_id', db.Integer, db.ForeignKey('games.id')),
                        db.Column('genre_id', db.Integer, db.ForeignKey('genres.id'))
                        )


class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    igdb_id = db.Column(db.BigInteger)
    name = db.Column(db.String(255))
    summary = db.Column(db.Text)
    rating = db.Column(db.SmallInteger)
    series_id = db.Column(db.Integer, db.ForeignKey('series.id'))
    series = db.relationship('Series', backref=db.backref('series', uselist=False))
    developer_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    developer = db.relationship('Company', backref=db.backref('developer', uselist=False))
    publisher_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    publisher = db.relationship('Company', backref=db.backref('publisher', uselist=False))
    release_date = db.Column(db.DateTime)
    genres = db.relationship('Genres', secondary=games_genres)
    cover = db.Column(db.String(255))
    screenshots = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now())


class Series(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    igdb_id = db.Column(db.BigInteger)
    created_at = db.Column(db.DateTime, default=datetime.now())


class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    igdb_id = db.Column(db.BigInteger)
    name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.now())


class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    igdb_id = db.Column(db.BigInteger)
    name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.now())


manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
