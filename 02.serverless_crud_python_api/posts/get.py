import json
from urllib.request import urlopen
from config import base_url


def get(event,context):
    id = event["id"]
    with urlopen(base_url + f"posts/{id}") as response:
        body = response.read()
        status =  response.getcode()   

    todo_item = json.loads(body)    
    
    return {
            'statusCode': status,
            'body': todo_item
        }

def getall(event,context):
    
    with urlopen(base_url + f"posts") as response:
        body = response.read()
        status =  response.getcode()   
    todo_item = json.loads(body)    
    
    return {
            'statusCode': status,
            'body': todo_item
        }

def getcomment(event,context):
    id = event["id"]
    with urlopen(base_url + f"posts/{id}/comments") as response:
        body = response.read()
        status =  response.getcode()   
    todo_item = json.loads(body)    
    
    return {
            'statusCode': status,
            'body': todo_item
        }


# {
#     title: 'foo',
#     body: 'bar',
#     userId: 1,
#   }