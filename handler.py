import json

def hello(event,context):
    body = {"message" : "my first test api with serverless",input: event}

    return {"status_code":200,"body": json.dumps(body)}

