from flask import Flask
from flask_mongoengine import Mongoengine
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


db = Mongoengine()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from endpoints.authentication.routes import users
    from endpoints.main.routes import jsonify

    return app
