# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
def post(to, code):
	account_sid = 'ACa22445815bbc53cde2b2f471fdd2ef46'
	auth_token = 'e5bf88c070bdda49a6c514f0b51e79f1'
	client = Client(account_sid, auth_token)
	try:
		verification_check = client.verify \
	                           .services('VA4ff03c64c0218ad19431a8594bc923bc') \
	                           .verification_checks \
	                           .create(to=to, code=code)

		if verification_check.status == "approved":
			return jsonify({'message': 'Verification Success'}), 200
		else:
			return jsonify({'message': 'The code you provided is incorrect'}), 400
	except Exception as e:
		raise e
	
