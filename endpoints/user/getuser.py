# End-point to fetch a user by it's unique Id element.

from models.user import User
from flask import jsonify

def getuser(userId):
    #Gets an userId or throws a 404 error message!
    user = User.objects.get_or_404(id=userId)
    #Jsonifies the fetched user details for the specific userId
    return jsonify(user)
  




    
