from functools import wraps
from flask import jsonify, request, g
from config import app, bcrypt
from models.user import User
import jwt
import datetime
import os
from dotenv import load_dotenv, find_dotenv

#locate and load .env file
load_dotenv(find_dotenv())


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
            data = jwt.decode(token, os.getenv('JWT_SECRET_KEY'))
            current_user = User.objects.get(id=data["id"])
        except:
            return jsonify({'message': 'INVALID TOKEN!'}), 401
        g.user = {'id': data["id"]}
        return f(*args, **kwargs)
    return decorated



def authVerify():
    auth = request.get_json()
    auth_pwd = auth.get('password')
    auth_email = auth.get('email')
    if not auth or not auth_email or not auth_pwd:
        return jsonify({
            'status':'unauthorized access',
            'WWW-Authenticate': 'Basic realm="login required!"'
            }), 401

    user = User.objects.get(email=auth_email)
    hashed_pwd = user.hash_password()
    # print("++++++++++")
    # print(hashed_pwd)
    # print("++++++++++")
    if user and bcrypt.check_password_hash(hashed_pwd, auth_pwd):
        try:
            payload = ({
                'id': str(user["id"]), #string instead of ObjectID
                'iat': datetime.datetime.utcnow(),
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                }) #60mins logged on session
            token = jwt.encode(payload, key=os.getenv('JWT_SECRET_KEY')).decode('UTF-8')
            user._set_user_token(token)
            return jsonify({
                'token':token,
                'session-limit': "60mins"}), 201 #token created
        except Exception as e:
                  return jsonify({
                      'response': 'could not generate user token',
                      'status':'fail'
                      })
    return jsonify({
        'status':'unauthorized access',
        'WWW-Authenticate': 'Invalid user credentials'}), 401  #if one of the login details is incorrect, return this