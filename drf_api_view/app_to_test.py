import requests

import json


url="http://127.0.0.1:8000/employee_api"


def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}

    headers={'content-type': 'application/json'}

    json_data=json.dumps(data)
    r=requests.get(url,data=json_data,headers=headers)

    print(r.json())

#
# get_data()

def post_data():
    data={
        "name":"rahul",
        "age":"20",
        "city":"San Francisco",
        "salary":10000
    }
    headers={'content-type': 'application/json'}
    json_data=json.dumps(data)
    r=requests.post(url,data=json_data,headers=headers)
    print(r.json())

def update_data():
    data={
        "id":1,
        'name':'ranjan_gupta'
    }
    headers={'content-type': 'application/json'}
    json_data=json.dumps(data)
    r=requests.put(url,data=json_data,headers=headers)
    print(r.json())

update_data()

# post_data()