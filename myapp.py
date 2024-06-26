import requests

# url="http://127.0.0.1:8000/drfadd/"
# # data={
#     'name':'snehsa wow',
#     'roll':120,
#     'city':'mumbai',
# }
#
# import json
#
# json_data=json.dumps(data)
#
# r=requests.post(url=url,data=json_data)
#
#
# data=r.json()
#
# print(data)
import json

# NOw to get data
url="http://127.0.0.1:8000/student_api"


def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}

    json_data=json.dumps(data)
    r=requests.get(url,data=json_data)

    print(r.json())


get_data()