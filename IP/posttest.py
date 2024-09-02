import requests
import random
import json
import string
import pytest

payload={
    "name": "Nitin",
    "job": "Automation"
    }

resp=requests.post("https://reqres.in/api/users",data=payload)
code=resp.status_code
json_data=resp.json()
json_str = json.dumps(json_data, indent=4)
print("json GET response body: ", json_str)
print(resp)
assert code==201,"Status Code doest Match"
assert resp.json()['job']=='Automation'
