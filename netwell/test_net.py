import pytest
import requests

# Define the login URL and data
login_url = "https://testfabric.carynhealth.com/api/v1/login"
login_data = {
    "username": "admin",
    "password": "x1TXVUtXL6PaBWam"
}

# Define the second API URL
api_url = "https://testfabric.carynhealth.com/api/v1/csrportal/empid/fetch"

# Define the headers
headers = {
    "Content-Type": "application/json"
}

# Define the payload for the second API
payload = {
    "empId": "444179417"
}

# Create a fixture to obtain the bearer token
@pytest.fixture
def bearer_token():
    response = requests.post(login_url, json=login_data)
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        raise Exception(f"Failed to get bearer token. Status code: {response.status_code}")

# Create a test to make the second API request with the bearer token
def test_second_post_api(bearer_token):
    headers["Authorization"] = f"Bearer {bearer_token}"
    headers["X-Tenant-Id"] = "TkVUV0VMTDtNb24gU2VwIDI1IDIwMjMgMTU6MjA6NTYgR01UKzA1MzAgKEluZGlhIFN0YW5kYXJkIFRpbWUp"

    response = requests.post(api_url, headers=headers, json=payload)

    assert response.status_code == 200, f"Request failed with status code {response.status_code}"

# To run the tests, use the following command in your terminal:
# pytest -v <filename>.py
