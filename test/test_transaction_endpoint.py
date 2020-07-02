import random
from unittest import TestCase
import unittest 
import requests
import json

test_instance_number = random.randint(0, 200000)
valid_entry_id = ''


class TestForTransactionEndpoint(TestCase):

    def test_transaction_res(self):
        response = requests.get('http://api-mycustomer-python.herokuapp.com/transaction/all')
        self.assertEqual(response.status_code, 200)

    def test_transaction_new_no_entry(self):
        # Ensures no input means 400 Error
        response = requests.post('http://api-mycustomer-python.herokuapp.com/transaction/new', headers={'Content-Type': 'application/json'})
        res = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(res['detail'], "None is not of type 'object'")

    def test_transaction_delete_invalid_ID(self):
        # Ensures invalid ID means 400 Error
        # Invalid here is ID != 24
        response = requests.delete('http://api-mycustomer-python.herokuapp.com/transaction/delete/4', headers={'Content-Type': 'application/json'})
        res = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(res, "Invalid input")

    def test_transaction_delete_nonexistent_ID(self):
        # Ensures wrong valid ID means 404 Error
        response = requests.delete('http://api-mycustomer-python.herokuapp.com/transaction/delete/5efa3305114a3a878c0fa182', headers={'Content-Type': 'application/json'})
        res = response.json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(res, "Transaction not found")

    def test_transaction_new_valid_entry(self):
        # Ensures valid input means 201
        data = {
            'amount': 0,
            'customer_phone_number': 'TEST_CUSTOMER_PHONE_NUMBER',
            'description': 'TEST_TRANSACTION_' + str(test_instance_number),
            'interest': 0,
            'store_name': 'TEST_SHOP_NAME',
            'total_amount': 0,
            'transaction_name': 'TEST_TRANSACTION_' + str(test_instance_number),
            'transaction_role': 'TEST_TRANSACTION_' + str(test_instance_number),
        }
        response = requests.post('http://api-mycustomer-python.herokuapp.com/transaction/new', headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        global valid_entry_id
        valid_entry_id = response.json()['result']['_id']['$oid']
        self.assertEqual(response.status_code, 201)

    def test_transaction_z_delete_valid_existent_ID(self):
        # Ensures valid entry can be deleted
        # the _z_ in the function name is to ensure this test runs last (after the new valid transaction)

        response = requests.delete(
            'http://api-mycustomer-python.herokuapp.com/transaction/delete/{}'.format(valid_entry_id),
            headers={'Content-Type': 'application/json'})
        res = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res, "Successful operation")


'''
    def test_transaction_new_entry_exist(self):

        #Ensures existed transaction inputs gives transaction already exists message

        data = {
            'amount': 0,
            'customer_phone_number': 'TEST_CUSTOMER_PHONE_NUMBER',
            'description': 'string',
            'interest': 0,  
            'store_name': 'TEST_SHOP_NAME',
            'total_amount': 0,
            'transaction_name': 'string',
            'transaction_role': 'string'
        }
        response = requests.post('http://api-mycustomer-python.herokuapp.com/transaction/new', headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        res = response.json()
        self.assertEqual(response.status_code, 403)
        self.assertEqual(res['message'], "transaction already exists")
'''


if __name__ == '__main__':
    unittest.main()

