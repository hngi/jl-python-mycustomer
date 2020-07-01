from models.complaint_form import Complaint
from flask import request, jsonify


def delete(complaintId):
    """
    Delete complaint instance with id=complaintId.
    """

    try:
        complaint = Complaint.objects.get(id=complaintId)

        complaint.delete()

    except Exception as e:
        return jsonify({"status": "failed",
                        "error": "complaint id not found",
                        "verbose": "{}".format(e)}), 404

    return jsonify({"status": "OK"}), 200
