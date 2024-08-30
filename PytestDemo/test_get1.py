import json

import requests


def test_get1():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)

    # Print the response status code and content
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())  # This will print the response in JSON format

    # Assert that the status code is 200
    assert response.status_code == 200
    # Parse the response JSON
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print(json_str)


def test_post1():
    base_url="https://reqres.in/api/users"
    payload={
        "name": "morpheus",
        "job": "leader"
    }


    response_post1=requests.post(base_url,payload)
    # Assert that the status code is 200
    assert  response_post1.status_code == 201
    print(response_post1.text)
    json_data=response_post1.json()
    json_str=json.dumps(json_data,indent=4)
    print(json_str)
