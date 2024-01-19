import json
# import requests

base_url = "https://jsonplaceholder.typicode.com/"

def hello(event,context):
    # resp = requests.get(url = base_url + "todo/1")
    body = {"message" : "my first test api with serverless","input": event}

    # return {"status_code":resp.status_code,"body": resp.json()}

import json
from urllib.request import urlopen
from config import base_url

def hello(event, context):
    # TODO implement
    url = "https://jsonplaceholder.typicode.com/todos/1"
    with urlopen(url) as response:
        body = response.read()
        status = response.getcode()
    
    todo_item = json.loads(body)
    
    return {
            'statusCode': status,
            'body': todo_item
        }

