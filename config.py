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


app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY')


app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

bcrypt = Bcrypt(app)


# mongodb database config
app.config["MONGODB_SETTINGS"] = {
    "host": os.getenv('MONDO_DB_HOST'),
    "connect": os.getenv('DB_CONNECT')
}

# initialize objects#
db = MongoEngine(app)

#todo: put the above in a function and return app