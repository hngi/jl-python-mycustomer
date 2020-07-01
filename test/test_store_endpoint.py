from unittest import TestCase
import unittest
import requests
import json

class Test_For_Store_Endpoint(TestCase):

    def test_store_res(self):
        response = requests.get('http://api-mycustomer-python.herokuapp.com/store/all')
        self.assertEqual(response.status_code, 200)

    def test_store_new_no_entry(self):

    	#Ensures no input means 400 Error
        
        response = requests.post('http://api-mycustomer-python.herokuapp.com/store/new', headers={'Content-Type': 'application/json'})
        res = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(res['detail'], "None is not of type 'object'")

    def test_store_new_valid_entry(self):

    	#Ensures valid input means 201
        #increment the digit for a new successful test run - testxxxx1 --> testxxxx2 --> and so on

        data = {
            'address': 'testaddr2', 
            'name': 'testname2',
            'email': 'testemail2', 
            'phone': 'testphone2',  
            'tagline': 'testtag2'
        }
        response = requests.post('http://api-mycustomer-python.herokuapp.com/store/new', headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        self.assertEqual(response.status_code, 201)

    def test_store_id_non_existent(self):

        #Nonexistent ID SHOULD GIVE 404 - UNABLE to find store

        response = requests.get('http://api-mycustomer-python.herokuapp.com/store/5efa3305114a3a878c0fa18x')
        self.assertEqual(response.status_code, 404)

    def test_store_new_entry_exist(self):

        #Ensures existed store inputs gives store already exists message

        data = {
            'phone': '8888883888',
            'email': 'strinsdsg',
            'address': 'sstrindssg',
            'name': 'strinsdsg', 
            'tagline': 'strissdng'
        }
        response = requests.post('http://api-mycustomer-python.herokuapp.com/store/new', headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        res = response.json()
        self.assertEqual(response.status_code, 403)
        self.assertEqual(res['message'], "Store already exists")

if __name__ == '__main__':
    unittest.main()