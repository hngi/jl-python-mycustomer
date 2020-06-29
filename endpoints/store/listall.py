# End-point for fetching store list.

from flask import jsonify
from models.store import Store


#Function to fetch store list
def get():
    #Getting all stores from the database
    stores = Store.objects.all()
    #Jsonifies all store details
    return jsonify(stores)
