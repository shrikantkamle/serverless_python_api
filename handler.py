import json
import requests

base_url = "https://jsonplaceholder.typicode.com/"

def hello(event,context):
    resp = requests.get(url = base_url + "/todo/1")
    # body = {"message" : "my first test api with serverless","input": event}

    return {"status_code":resp.status_code,"body": resp.json()}

