from unittest import TestCase
import unittest
import requests
import random
import json

test_instance_number = random.randint(0, 200000)
valid_entry_id = ''
base_url = 'http://api-mycustomer-python.herokuapp.com'
# base_url = 'http://127.0.0.1:5207'  # uncomment to test on your local server


class TestsForUserEndpoint(TestCase):

    def test_user_get_all(self):
        response = requests.get(base_url + '/user/all')
        self.assertEqual(response.status_code, 200)

    def test_user_new_no_entry(self):
        # Ensures no input means 400 Error
        response = requests.post(base_url + '/user/new', headers={'Content-Type': 'application/json'})
        res = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(res['detail'], "None is not of type 'object'")

    def test_user_za_new_valid_entry(self):
        # Ensures valid input means 200
        data = {
            'email': 'TEST_USER_EMAIL_' + str(test_instance_number),
            'first_name': 'TEST_FIRST_NAME_' + str(test_instance_number),
            'last_name': 'TEST_LAST_NAME_' + str(test_instance_number),
            'password': 'TEST_PASSWORD_' + str(test_instance_number),
            'phone_number': 'TEST_PHONE_NUMBER_' + str(test_instance_number)
        }
        response = requests.post(base_url + '/user/new',
                                 headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        global valid_entry_id
        valid_entry_id = response.json()['result']['_id']['$oid']
        self.assertEqual(response.status_code, 201)

    def test_user_get_invalid_id(self):
        # Ensures invalid ID gives 404 error
        response = requests.get(base_url + '/user/1')
        self.assertEqual(response.status_code, 404)

    def test_user_zb_get_valid_id(self):
        # Ensures valid ID gives 200
        response = requests.get(base_url + '/user/{}'.format(valid_entry_id))
        self.assertEqual(response.status_code, 200)

    def test_user_zc_new_valid_entry_exist(self):
        # Ensures existed user inputs gives store already exists message
        data = {
            'email': 'TEST_USER_EMAIL_' + str(test_instance_number),
            'first_name': 'TEST_FIRST_NAME_' + str(test_instance_number),
            'last_name': 'TEST_LAST_NAME_' + str(test_instance_number),
            'password': 'TEST_PASSWORD_' + str(test_instance_number),
            'phone_number': 'TEST_PHONE_NUMBER_' + str(test_instance_number)
        }
        response = requests.post(base_url + '/user/new',
                                 headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        res = response.json()
        self.assertEqual(response.status_code, 403)
        self.assertEqual(res['message'], "User already exists")

    # todo: uncomment when /user/delete is set up
    # def test_user_zd_delete_valid_existent_ID(self):
    #     # Ensures valid entry can be deleted
    #     # the _z_ in the function name is to ensure this test runs last (after the new valid store)
    #     response = requests.delete(base_url + '/user/delete/{}'.format(valid_entry_id),
    #                                headers={'Content-Type': 'application/json'})
    #     res = response.json()
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(res['message'], "User deleted successfully")


if __name__ == '__main__':
    unittest.main()