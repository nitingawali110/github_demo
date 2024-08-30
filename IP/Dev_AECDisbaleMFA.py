import json
import pytest
import requests

# Define the base URLs for the APIs
login_url = "https://dev.fabric.carynhealth.com/api/v1/login"
csrportal_url = "https://dev.fabric.carynhealth.com/api/v1/csrportal/disablemfa"

# Credentials for login
login_payload = {
    "username": "maricopa",
    "password": "QPvcY0n#S1u"
}


# Pytest fixture to get the bearer token
@pytest.fixture
def bearer_token():
    # Send a POST request to the login API to obtain the token
    login_response = requests.post(login_url, json=login_payload)

    # Ensure a successful response
    assert login_response.status_code == 200, "Login request failed"

    # Extract the bearer token from the response headers
    bearer_token = login_response.headers.get("Authorization")

    return bearer_token


# Pytest test function to test the second API
def test_disable_mfa_with_token(bearer_token):
    # Define the payload for the second API
    csrportal_payload = {
        "cognitoUserPool": "us-east-2_eHmPpZxv7",
        "username": "devtestnitin31@yopmail.com"
    }

    # Define headers with the bearer token
    headers = {
        "Authorization": bearer_token
    }

    # Send a POST request to the second API with the bearer token
    response = requests.post(csrportal_url, json=csrportal_payload, headers=headers)
    print(response.text)
    # Ensure a successful response
    # assert response.status_code == 200, "API request failed"

    # Your assertions on the response data can be added here

    # For example, if you want to check if the response contains certain data:
    # response_data = response.json()
    # json_data = response_data.json()
    # json_str = json.dumps(json_data, indent=4)
    # print("Member Portal Details: ", json_str)
