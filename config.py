import os.path
import connexion
from flask_mongoengine import MongoEngine
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv, find_dotenv

#locate and load .env file
load_dotenv(find_dotenv())


base_dir = os.path.abspath(os.path.dirname(__file__))
connex_app = connexion.App(__name__, specification_dir=base_dir)
app = connex_app.app


# app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
# app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY')


app.config['SECRET_KEY'] = "hcdsfbhfTHIS_IS_TO_AVOID_SERVER_BREAK"
app.config["JWT_SECRET_KEY"] = "hcdsfbhfTHIS_IS_TO_AVOID_SERVER_BREAKDDDD"


app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

bcrypt = Bcrypt(app)


# mongodb database config
app.config["MONGODB_SETTINGS"] = {
    "host": "mongodb://austino:hngi7task4@cluster0-shard-00-00-qht2p.mongodb.net:27017,cluster0-shard-00-01-qht2p.mongodb.net:27017,cluster0-shard-00-02-qht2p.mongodb.net:27017/MyCustomer?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority",
    "connect": False
}

# initialize objects#
db = MongoEngine(app)

#todo: put the above in a function and return app