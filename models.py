from flask_login import UserMixin
from test import db


film_actor = db.Table('film_actor', db.Model.metadata,
    db.Column('film_id', db.Integer, db.ForeignKey('film.id')),
    db.Column('actor_id', db.Integer, db.ForeignKey('actor.id'))
)

film_seans = db.Table('film_seans', db.Model.metadata,
    db.Column('film_id', db.Integer, db.ForeignKey('film.id')),
    db.Column('seans_id', db.Integer, db.ForeignKey('seans.id'))
)

seans_palce = db.Table('seans_place ', db.Model.metadata,
    db.Column('seans_id', db.Integer, db.ForeignKey('seans.id')),
    db.Column('place_id', db.Integer, db.ForeignKey('place.id'))
)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Film(db.Model):
    __tablename__ = 'film'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500))
    score = db.Column(db.Integer)
    actor = db.relationship("Actor", secondary=film_actor, backref="actor")
    seans = db.relationship("Seans", secondary=film_seans, backref="seans")
    comments = db.Column(db.String(100))


class Actor(db.Model):
    __tablename__ = 'actor'
    id = db.Column(db.Integer, primary_key=True)
    # film = db.relationship("Film", secondary="films", backref="actor")
    name = db.Column(db.String(30))
    surname = db.Column(db.String(30))


class Seans(db.Model):
    __tablename__ = 'seans'
    id = db.Column(db.Integer, primary_key=True)
    # film = db.relationship("Film", secondary="films", backref="seans")
    place = db.relationship("Place", secondary=seans_palce, backref="seans")
    datetime = db.Column(db.DateTime)


class Place(db.Model):
    __tablename__ = 'place'
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    isBusy = db.Column(db.BOOLEAN)
    # seans = db.relationship("Place", secondary="seans", backref="place")
