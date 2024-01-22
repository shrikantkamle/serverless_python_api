import json
from urllib.request import urlopen,Request
from config import base_url
import urllib.parse


def add(event,context):
    id = event["id"]
    print("received: ", id)
    # Get the data from the API
    data = urllib.parse.urlencode(event).encode()
    req = Request(url = base_url + f"posts",data= data)
    res = urlopen(req)
    body = res.read()
    status =  res.getcode()  
    
    return {
            'statusCode': status,
            'body': body
        }

# data = urllib.parse.urlencode(values)
# req = urllib.request.Request(url, data, headers)
# response = urllib.request.urlopen(req)
# the_page = response.read()