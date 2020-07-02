# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
def post(to, code):
	account_sid = 'Your account_sid'
	auth_token = 'Your auth_token'
	client = Client(account_sid, auth_token)
	try:
		verification_check = client.verify \
	                           .services('Your service_sid') \
	                           .verification_checks \
	                           .create(to=to, code=code)

		if verification_check.status == "approved":
			return jsonify({'message': 'Verification Success'}), 200
		else:
			return jsonify({'message': 'The code you provided is incorrect'}), 400
	except Exception as e:
		raise e
	
