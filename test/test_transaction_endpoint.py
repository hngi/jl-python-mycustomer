from unittest import TestCase
import unittest 
import requests
import json

class Test_For_Transaction_Endpoint(TestCase):

    def test_transaction_res(self):
        response = requests.get('http://api-mycustomer-python.herokuapp.com/transaction/all')
        self.assertEqual(response.status_code, 200)

    def test_transaction_new_no_entry(self):

    	#Ensures no input means 400 Error
        
        response = requests.post('http://api-mycustomer-python.herokuapp.com/transaction/new', headers={'Content-Type': 'application/json'})
        res = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(res['detail'], "None is not of type 'object'")

    def test_transaction_delete_invalid_ID(self):

        #Ensures invalid ID means 400 Error
        #Invalid here is ID != 24
        
        response = requests.delete('http://api-mycustomer-python.herokuapp.com/transaction/delete/4', headers={'Content-Type': 'application/json'})
        res = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(res, "Invalid input")

    def test_transaction_delete_ID(self):

        #Ensures wrong valid ID means 404 Error
        
        response = requests.delete('http://api-mycustomer-python.herokuapp.com/transaction/delete/5efa3305114a3a878c0fa182', headers={'Content-Type': 'application/json'})
        res = response.json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(res, "Transaction not found")
        
    """
    def test_transaction_new_valid_entry(self):

    	#Ensures valid input means 201
        #Ensure to change the all value for each key when running this test again for success!!

        data = {
            'amount': 0,
            'customer_phone_number': 0,
            'description': 'string',
            'interest': 0,
            'store_name': 'string',
            'total_amount': 0,
            'transaction_name': 'string',
            'transaction_role': 'string'
        }
        response = requests.post('http://api-mycustomer-python.herokuapp.com/transaction/new', headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        self.assertEqual(response.status_code, 201)

    def test_transaction_new_entry_exist(self):

        #Ensures existed transaction inputs gives transaction already exists message

        data = {
            'amount': 0,
            'customer_phone_number': 0,
            'description': 'string',
            'interest': 0,  
            'store_name': 'string',
            'total_amount': 0,
            'transaction_name': 'string',
            'transaction_role': 'string'
        }
        response = requests.post('http://api-mycustomer-python.herokuapp.com/transaction/new', headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        res = response.json()
        self.assertEqual(response.status_code, 403)
        self.assertEqual(res['message'], "transaction already exists")
    """

if __name__ == '__main__':
    unittest.main()