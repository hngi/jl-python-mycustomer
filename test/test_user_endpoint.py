from unittest import TestCase

import requests
import json

class Test_For_User_Endpoints(TestCase):
    def test_user_res(self):
        response = requests.get('http://api-mycustomer-python.herokuapp.com/user/all')
        self.assertEqual(response.status_code, 200)

    def test_user_new_no_entry(self):

    	#Ensures no input means 400 Error
        
        response = requests.post('http://api-mycustomer-python.herokuapp.com/user/new', headers={'Content-Type': 'application/json'})
        res = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(res['detail'], "None is not of type 'object'")

    def test_user_new_valid_entry(self):

    	#Ensures valid input means 200 
        #Ensure to change the email when running this test again for success!!! 
        #Ensure to change the Number when running this test again for success!!!

        data = {
            'email': 'jbjwbh@domain.com',
            'first_name': 'Mikah',
            'last_name': 'Mikah',
            'password': 'string',
            'phone_number': '56645453454'
        }
        response = requests.post('http://api-mycustomer-python.herokuapp.com/user/new', headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        self.assertEqual(response.status_code, 200)

    def test_user_id(self):

        #Ensure wrong ID gives 404 error

        response = requests.get('http://api-mycustomer-python.herokuapp.com/user/1')
        self.assertEqual(response.status_code, 404)