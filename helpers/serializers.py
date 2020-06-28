import json


def json_serializer(mongodb_object):
    """serialize mongodb object to python dictionary style json data"""
    json_raw = mongodb_object.to_json()
    python_dict = json.loads(json_raw)

    return python_dict
