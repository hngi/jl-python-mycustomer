from flask import jsonify


def greet(name='world'):
    return jsonify('Hello {}!'.format(name))
