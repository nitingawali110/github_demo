import json

import pytest
import requests


# TC1 Verify the creation Booking
@pytest.mark.crud
def test_create_booking_positive():
    # Request
    # URL
    # Method
    # Headers
    # payload
    # Auth
    # Auth in Post
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2013-02-23",
            "checkout": "2014-10-23"
        },
        "additionalneeds": "Breakfast"
    }

    response=requests.post(url=URL,headers=headers,json=payload,)
    # Response body Verifications
    # Headers
    # Status Code
    # JSON Schema Validation
    # Time Response

    assert response.status_code==200
    # print(headers)
    print(response.text)
    json_response=json.loads(response.text)
    print(json.dumps(json_response,indent=4,sort_keys=True))
    response_json=response.json()
    booking_id=response_json["bookingid"]
    assert booking_id is not None
    assert booking_id > 0
    assert type(booking_id)==int
    first_name=response_json["booking"]["firstname"]
    assert first_name=="Amit"
    return booking_id


#TC2 Verify Booking is not created
def test_create_booking_neagtive():
    # Request
    # URL
    # Method
    # Headers
    # payload
    # Auth
    # Auth in Post
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {}

    response = requests.post(url=URL, headers=headers, json=payload, )
    # Response body Verifications
    # Headers
    # Status Code
    # JSON Schema Validation
    # Time Response

    assert response.status_code == 200

