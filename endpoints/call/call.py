# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure]\
def post(customer_phone_number):
	account_sid = 'Your account_sid'
	auth_token = 'Your auth_token'
	client = Client(account_sid, auth_token)
	try:
		call = client.calls.create(
	        twiml='<Response><Say>Welcome to MyCustomer</Say></Response>',
	        to=customer_phone_number,
	        from_='Your trial number'
	    )
		return jsonify({'message': 'Call Success', 'call.sid': call.sid}), 200
	except Exception as e:
		return jsonify({'message': 'Call Failure', 'error': e}), 405
	
 

	
