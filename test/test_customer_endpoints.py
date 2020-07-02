from unittest import TestCase
import unittest
import random
import requests
import json

test_instance_number = random.randint(0, 200000)
valid_entry_id = ''


class TestForCustomerEndpoint(TestCase):

    def test_customer_res(self):
        response = requests.get('http://api-mycustomer-python.herokuapp.com/customer/all')
        self.assertEqual(response.status_code, 200)

    def test_customer_new_no_entry(self):
        # No input should raise 400 Error
        response = requests.post('http://api-mycustomer-python.herokuapp.com/customer/new', headers={'Content-Type': 'application/json'})
        res = response.json()
        self.assertEqual(response.status_code, 400)

    def test_customer_za_new_valid_entry(self):
        # Creating a new customer with valid details should give 201 status response
        # _za_ in function name is to make this run before the two below
        data = {
            'name': 'TEST_CUSTOMER_NAME_' + str(test_instance_number),
            'phone': 'TEST_CUSTOMER_PHONE_NUMBER_' + str(test_instance_number),
        }
        response = requests.post('http://api-mycustomer-python.herokuapp.com/customer/new', headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        global valid_entry_id
        valid_entry_id = response.json()['result']['_id']['$oid']
        self.assertEqual(response.status_code, 201)

    def test_customer_get_valid_nonexistent_ID(self):
        # Nonexistent ID SHOULD GIVE 404 - UNABLE to find customer
        response = requests.get('http://api-mycustomer-python.herokuapp.com/customer/5ef9ec43cfa2de40afffffff')
        self.assertEqual(response.status_code, 404)

    def test_customer_zb_get_valid_existent_ID(self):
        # Existent id should give 200
        response = requests.get('http://api-mycustomer-python.herokuapp.com/customer/{}'.format(valid_entry_id))
        self.assertEqual(response.status_code, 200)

    def test_customer_zc_new_valid_entry_exist(self):
        # Existing customer details should raise 403 when trying to create new customers as customer already exists
        data = {
            'name': 'TEST_CUSTOMER_NAME_' + str(test_instance_number),
            'phone': 'TEST_CUSTOMER_PHONE_NUMBER_' + str(test_instance_number),
        }
        response = requests.post('http://api-mycustomer-python.herokuapp.com/customer/new',
                                 headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        self.assertEqual(response.status_code, 403)

    # Uncomment this when /customer/delete/{} is set up
    #
    # def test_customer_zd_delete_valid_existent_ID(self):
    #     # Ensures valid entry can be deleted
    #     # the _z_ in the function name is to ensure this test runs last (after the new valid store)
    #     response = requests.delete(
    #         'http://api-mycustomer-python.herokuapp.com/customer/delete/{}'.format(valid_entry_id),
    #         headers={'Content-Type': 'application/json'})
    #     res = response.json()
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(res['message'], "Customer deleted successfully")


if __name__ == '__main__':
    unittest.main()

