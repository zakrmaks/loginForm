from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from populate import initial_populate

db = SQLAlchemy()



def initial_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
    db.session.add_all(initial_populate())
    db.session.commit()
    return db


