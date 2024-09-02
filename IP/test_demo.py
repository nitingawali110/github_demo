import requests
import random
import json
import string
import pytest

#baseurl;
base_url="https://reqres.in/api/users?page=2"

# GET Request

def test_getrequest():
    url=base_url
    print("GET URL:",url)
    response= requests.get(url)
    assert response.status_code == 200,   "Status code is not 200"
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json GET response body: ", json_str)
    print("Employer Email:",json_data["data"][0]["email"])
    print(".......=====================.......")



def test_postrequest():

    payload={
    "name": "Nitin",
    "job": "Automation"
    }

    posturl="https://reqres.in/api/users"
    print("POST URL:",posturl)
    response= requests.post("https://reqres.in/api/users",data=payload)
    code=response.status_code
    json_data=response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json post response body: ", json_str)
    print(response)
    assert code==201,"Status Code doest Match"
    assert response.json()['job']=='Automation'


test_getrequest()
test_postrequest()

# def test_1():
#     x=10
#     y=10
#     z=x+y
#     assert x==y
#     print("x+y:",z)


# def test_2():
#     name="Nitin"
#     title="This is Test Nitin file"
#     assert name in title




#call

# test_1()
# test_2()
