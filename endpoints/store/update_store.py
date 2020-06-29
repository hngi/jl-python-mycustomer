from flask import jsonify
from models.store import Store


def updateStore(storeId):

    store = Store.objects.get(id=storeId)
    exists = storeId in Store
    store['id'] = storeId
    if exists:
        Store[storeId].update(store)
    else:
        Store[storeId] = store
    return jsonify({ "status": "OK" }), 200
