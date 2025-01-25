import pytest
import requests
import json


def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}

    json_payload = {
        "username": "admin",
        "password": "password123"
    }

    response = requests.post(url=url, headers=headers, json=json_payload)
    data = response.json()
    token = data["token"]
    print(token)
    return token


def create_booking():
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

    response = requests.post(url=URL, headers=headers, json=payload)

    assert response.status_code == 200  # Corrected to 201 for creation
    print(response.text)

    json_response = response.json()
    print(json.dumps(json_response, indent=4, sort_keys=True))

    booking_id = json_response["bookingid"]
    assert booking_id is not None
    assert booking_id > 0
    assert isinstance(booking_id, int)

    first_name = json_response["booking"]["firstname"]
    assert first_name == "Amit"

    return booking_id


def test_put_request():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"
    param = create_booking()
    PUTURL = base_url + base_path + str(param)

    token = create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={token}"
    }

    print(headers)

    json_payload = {
        "firstname": "Nitin",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2013-02-23",
            "checkout": "2014-10-23"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url=PUTURL, headers=headers, json=json_payload)
    assert response.status_code == 200

    data = response.json()
    assert data["firstname"] == "Nitin", "Failed Message - Incorrect First Name"
