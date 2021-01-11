from models import *
from datetime import datetime



def initial_populate():
    film = Film(description='test description', score=5, comments="test")
    actor = Actor(name='Djon', surname='Wash')
    seans = Seans(datetime=datetime.today())
    place = Place(price=200, isBusy=True)
    place2 = Place(price=300, isBusy=True)
    place3 = Place(price=400, isBusy=False)

    film.actor.append(actor)
    return [film, actor, seans, place, place2, place3]
