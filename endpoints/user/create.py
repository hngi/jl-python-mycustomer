from mongoengine import NotUniqueError
from models.user import User
from flask import jsonify


def post(body):
    """
    POST response method for creating user.
    :return: JSON object
    """
    try:
        post_user = User(**body)
        post_user.save()
    except NotUniqueError:
        return jsonify({'status': 'failure', 'message': 'User already exists'}), 403
    except KeyError:
        return jsonify({'status': 'failure', 'message': 'Invalid key supplied'}), 405
    except Exception as e:
        return jsonify({'status': 'failure', 'message': 'Something went wrong while adding customer'}), 500

    return jsonify({'status': 'success',
                    'message': 'User created successfully',
                    'result': post_user}), 201

