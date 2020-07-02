
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
def post(to,channel='sms'):
	account_sid = 'Your account_sid'
	auth_token = 'Your auth_token'
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