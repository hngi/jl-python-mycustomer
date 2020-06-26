import os.path
import secrets
import connexion

from flask_mongoengine import MongoEngine
# from flask_marshmallow import Marshmallow  # for validating db models; don't know if this works with mongo

base_dir = os.path.abspath(os.path.dirname(__file__))

connex_app = connexion.App(__name__, specification_dir=base_dir)
app = connex_app.app

app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# initialize objects
db = MongoEngine(app)
# ma = Marshmallow(app)

# mongodb database config
app.config["MONGODB_SETTINGS"] = {
    "host": "mongodb+srv://austino:hngi7task4@cluster0-qht2p.mongodb.net/<MyCustomer>?retryWrites=true&w=majority",
    "connect": False
}
