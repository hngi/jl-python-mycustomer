from flask import jsonify, request
from models.store import Store


def updateStore(storeId):

    data = request.get_json()
    store = Store.objects.get(id=storeId)
    exists = storeId in Store
    store['id'] = storeId
    if exists:
        Store[data].update()
    else:
        Store[storeId] = store
    return jsonify({ "status": "OK" }), 200
