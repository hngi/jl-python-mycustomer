
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
def post(to,channel='sms'):
	account_sid = 'ACa22445815bbc53cde2b2f471fdd2ef46'
	auth_token = 'e5bf88c070bdda49a6c514f0b51e79f1'
	client = Client(account_sid, auth_token)
	try:
		service = client.verify.services.create(friendly_name='MyCustomer')
		verification = client.verify \
		            		 .services('Your service_sid') \
		                     .verifications \
		                     .create(to=to, channel=channel)

		return jsonify({'verification.sid': verification.sid,
						'status' : verification.status }), 200
	except Exception as e:
		raise e
