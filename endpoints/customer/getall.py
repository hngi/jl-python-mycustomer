from flask import jsonify, request
from models.customer import Customer

def getAll():
    all_customers = Customer.objects.all()
    if all_customers:
        return jsonify({'Customers':all_customers}), 200
    return jsonify({'status':'failed'}), 400