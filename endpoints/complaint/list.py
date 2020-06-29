from flask import jsonify
from models.complaint_form import Complaint
from helpers.serializers import json_serializer


def get():
    complaints = Complaint.objects.all()
    return complaints