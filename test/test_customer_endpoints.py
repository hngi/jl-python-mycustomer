from unittest import TestCase
import unittest
import requests
import json


class TestForCustomerEndpoint(TestCase):

    def test_customer_res(self):
        response = requests.get('http://api-mycustomer-python.herokuapp.com/customer/all')
        self.assertEqual(response.status_code, 200)

    def test_customer_new_no_entry(self):

    	#No input should raise 400 Error
        response = requests.post('http://api-mycustomer-python.herokuapp.com/customer/new', headers={'Content-Type': 'application/json'})
        res = response.json()
        self.assertEqual(response.status_code, 400)

#uncomment the below function when authentication gets pushed so as to auto fill store_ref_id
    # def test_customer_new_valid_entry(self):

    # 	#Creating a new customer with valid details should give 201 status response
    #     #increment the digit for a new successful test run - testxxxx1 --> testxxxx2 --> and so on

    #     data = {
    #         'name': 'testname1', 
    #         'phone': 'testphone1',
    #     }
    #     response = requests.post('http://api-mycustomer-python.herokuapp.com/customer/new', headers={'Content-Type': 'application/json'}, data=json.dumps(data))
    #     self.assertEqual(response.status_code, 201)

    def test_customer_nonexistent_ID(self):
        #Nonexistent ID SHOULD GIVE 404 - UNABLE to find customer

        response = requests.get('http://api-mycustomer-python.herokuapp.com/customer/5ef9ec43cfa2de40afb2a1xx')
        self.assertEqual(response.status_code, 404)


    def test_customer_existent_ID(self):
        #as of now, 01/06/20 - 5ef9ec43cfa2de40afb2a176 exists
        response = requests.get('http://api-mycustomer-python.herokuapp.com/customer/5ef9ec43cfa2de40afb2a176')
        self.assertEqual(response.status_code, 200)


#uncomment this when name and phone are set as unique fields in the model
    # def test_customer_new_entry_exist(self):
    #     #Existing customer details should raise 403 when trying to create new customers as customer already exists

    #     data = {
    #         'phone': 'testphone1',
    #         'name': 'testname1',

    #     }
    #     response = requests.post('http://api-mycustomer-python.herokuapp.com/customer/new', headers={'Content-Type': 'application/json'}, data=json.dumps(data))
    #     res = response.json()
    #     self.assertEqual(response.status_code, 403)


if __name__ == '__main__':
    unittest.main()