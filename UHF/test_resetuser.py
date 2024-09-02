import json
import pytest
import requests

# Define the base URLs for the APIs
login_url = "https://dev.fabric.carynhealth.com/api/v1/login"
reset_url = "https://dev.fabric.carynhealth.com/api/v1/csrportal/resetuser"

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

# Pytest test function to test member portal registration with token
def test_resetuser(bearer_token):
    # Define the payload for member portal registration
    reset_payload = {
    "cognitoUserPool":"us-east-2_5Jn7qamnM",
    "username":"rohitthrive@yopmail.com"
    }

    # Define headers with the bearer token
    headers = {
        "Authorization": bearer_token
    }

    # Send a POST request to the member portal registration API with the bearer token
    response = requests.post(reset_url, json=reset_payload, headers=headers)

    # Ensure a successful response
    assert response.status_code == 200, "Registration request failed"
    # Parse the response JSON
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("member_portal_reset_user: ", json_str)




