from datetime import datetime
from flask import jsonify, request
from models.store import Store
from flask_mongoengine import mongoengine


def update(storeId):
    if len(storeId) != 24:
        return jsonify("Invalid ID supplied"), 400
    try:
        data = request.get_json()
        value = {
            "shop_address": data["address"],
            "store_name": data["name"],
            "tagline": data["tagline"],
            "phone_number": data["phone"],
            "email": data["email"],
           # "updated_at": datetime.utcnow()
        }
        val = Store.objects(id=storeId).update(**value)
        return jsonify({"Success": "Store updated"}), 200
    except KeyError as q:
        return jsonify({"Error": "Invalid ID"}), 400
    except mongoengine.errors.DoesNotExist as e:
        return jsonify({"Error": "Store not found"}), 404
    except mongoengine.errors.ValidationError as e:
        return jsonify("Validation exception"), 405