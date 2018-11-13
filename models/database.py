from datetime import datetime

from server import db


games_genres = db.Table('games_genres', db.Model.metadata,
                        db.Column('game_id', db.Integer, db.ForeignKey('games.id')),
                        db.Column('genre_id', db.Integer, db.ForeignKey('genres.id'))
                        )


class Series(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    igdb_id = db.Column(db.BigInteger)
    name = db.Column(db.String(255))
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
    release_date = db.Column(db.BigInteger)
    genres = db.relationship('Genres', secondary=games_genres)
    cover = db.Column(db.String(255))
    screenshots = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now())
