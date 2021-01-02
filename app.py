from flask import Flask
from auth import auth as auth_blueprint
from main import main as main_blueprint
# init SQLAlchemy so we can use it later in our models


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret-key-goes-here'

app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app

app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    app.run()
