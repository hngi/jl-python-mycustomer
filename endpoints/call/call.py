# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure]\
def post(customer_phone_number):
	account_sid = 'ACa22445815bbc53cde2b2f471fdd2ef46'
	auth_token = 'e5bf88c070bdda49a6c514f0b51e79f1'
	client = Client(account_sid, auth_token)
	try:
		call = client.calls.create(
	        twiml='<Response><Say>Welcome to MyCustomer Services, How can we help you</Say></Response>',
	        to=customer_phone_number,
	        from_='+12028311667'
	    )
		return jsonify({'message': 'Call Success', 'call.sid': call.sid}), 200
	except Exception as e:
		return jsonify({'message': 'Call Failure', 'error': e}), 405
	
 

	
