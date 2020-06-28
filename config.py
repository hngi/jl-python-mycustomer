import os.path
import connexion
from flask_mongoengine import MongoEngine
from flask_bcrypt import Bcrypt

base_dir = os.path.abspath(os.path.dirname(__file__))
connex_app = connexion.App(__name__, specification_dir=base_dir)
app = connex_app.app

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# mongodb database config
app.config["MONGODB_SETTINGS"] = {
    "host": "mongodb://austino:hngi7task4@cluster0-shard-00-00-qht2p.mongodb.net:27017,cluster0-shard-00-01-qht2p.mongodb.net:27017,cluster0-shard-00-02-qht2p.mongodb.net:27017/MyCustomer?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority",
    "connect": False
}

# initialize objects#
db = MongoEngine(app)


# For authentication 
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


