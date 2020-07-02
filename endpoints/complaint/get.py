from flask import jsonify
from models.complaint_form import Complaint


def getComplaint(complaintId):
    complaint = Complaint.objects.get_or_404(id=complaintId)
    
    return jsonify({"Success": complaint}), 200
