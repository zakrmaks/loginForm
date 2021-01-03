from flask import Flask
from auth import auth as auth_blueprint
from main import main as main_blueprint
from models import initial_db, User
from flask_login import LoginManager

# init SQLAlchemy so we can use it later in our models


app = Flask(__name__)
initial_db(app)
app.config['SECRET_KEY'] = 'secret-key-goes-here'



login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app

app.register_blueprint(main_blueprint)


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))

if __name__ == '__main__':
    app.run()
