from models.complaint_form import Complaint
from flask import request, jsonify


def update(complaintId):
    """
    Update complaint instance with id=complaintId.
    
    Editable fields of the database are 'message' and 'status'.
    """

    try:
        complaint = Complaint.objects.get(id=complaintId)

        complaint.message = request.get_json()["message"] or complaint.message
        complaint.status = request.get_json()["status"] or complaint.status
        complaint.save()

    except Exception as e:
        return jsonify({"status": "failed",
                        "error": "complaint id not found",
                        "verbose": "{}".format(e)}), 404

    return jsonify({"status": "OK"}), 200
