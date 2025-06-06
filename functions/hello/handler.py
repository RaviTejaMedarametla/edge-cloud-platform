import json

def handle(req):
    return json.dumps({"message": "Hello from OpenFaaS"})
