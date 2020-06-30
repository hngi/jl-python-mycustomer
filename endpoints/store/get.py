from flask import jsonify
from models.store import Store


def getStoreById(storeId):

    store = Store.objects.get(id=storeId)
    if store:
        return jsonify({"Store": store}), 200
    return jsonify({"msg":"Store not found"}), 404


