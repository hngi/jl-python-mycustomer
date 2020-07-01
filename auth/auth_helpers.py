from functools import wraps
from flask import jsonify, request, g
from config import app, bcrypt
from models.user import User
import jwt
# from werkzeug.security import generate_password_hash, check_password_hash
import datetime


#decorator to handle auth
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers or 'Authentication' in request.headers:
            token = request.headers['x-access-token'] or request.headers['Authentication']
        if not token:
            return jsonify({'message': 'UNAUTHORIZED ACCESS. TOKEN REQUIRED!'}), 401
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"])
            current_user = User.objects.get(id=data["id"])
        except:
            return jsonify({'message': 'INVALID TOKEN API!'}), 401
        g.user = {'id': data["id"]}
        return f(*args, **kwargs)
    return decorated



def authVerify():
    auth = request.get_json()
    auth_pwd = auth.get('password')
    auth_email = auth.get('email')
    if not auth or not auth_email or not auth_pwd:
        return jsonify(
            {'status':'unauthorized access',
             'WWW-Authenticate': 'Basic realm="login required!"'}), 401
    user = User.objects.get(email=auth_email)
    hashed_pwd = user.hash_password()
    # print("++++++++++")
    # print(hashed_pwd)
    # print("++++++++++")
    if user and bcrypt.check_password_hash(hashed_pwd, auth["password"]):
        payload = ({
            'id': str(user["id"]), #string instead of ObjectID
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            }) #60mins logged on session
        token = jwt.encode(payload, key=app.config['SECRET_KEY'])
        return jsonify({
            'token':token.decode('UTF-8'),
            'session-allowed': payload['exp']}), 201 #token created

    return jsonify(
            {'status':'unauthorized access',
             'WWW-Authenticate': 'Basic realm="login required!"'}), 401