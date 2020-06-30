from models.complaint_form import Complaint
from models.user import User
from models.user_store import UserStore
from flask import request, jsonify

def post():
    """
    POST response method for creating a complaint.
    :return: JSON object
    """
    data = request.get_json()
    post_complaint = Complaint(**data)
    post_complaint.save()
    output = {'id': str(post_complaint.id)}
    return jsonify({'result': output})
