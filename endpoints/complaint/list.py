from flask import jsonify
from models.complaint_form import Complaint


def get():
    complaints = Complaint.objects.all()
    return jsonify(complaints)