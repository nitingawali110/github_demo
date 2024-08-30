import json
import pytest
import requests

# Define the base URL for the APIs
base_url = "https://testfabric.carynhealth.com/api/v1/"

# Credentials for login
login_payload = {
    "username": "Innovation",
    "password": "IxLTA0LTI2VDExOjI4OjI4Wg=="
}
# Pytest fixture to get the bearer token
@pytest.fixture
def bearer_token():
    # Send a POST request to the login API
    login_response = requests.post(base_url + "login", json=login_payload)

    # Ensure a successful response
    assert login_response.status_code == 200, "Login request failed"

    # Extract the bearer token from the response headers
    bearer_token = login_response.headers.get("Authorization")
    return bearer_token


# Pytest test function to test the second API
@pytest.fixture
def test_fetch_emp_data_with_token(bearer_token):
    # Define the payload for the second API
    emp_payload = {
        "empId": "G839968"
    }
    # Define headers with the bearer token
    headers = {
        "Authorization": bearer_token,
        "X-Tenant-Id":"SU5OT1ZBVElPTjtTYXQgRmViIDE3IDIwMjQgMjM6MDQ6MDkgR01UKzA1MzAgKEluZGlhIFN0YW5kYXJkIFRpbWUp"
    }

    # Send a POST request to the second API with the bearer token
    response = requests.post(base_url + "csrportal/empid/fetch", json=emp_payload, headers=headers)

    # Ensure a successful response
    assert response.status_code == 200, "API request failed"

    # Your assertions on the response data can be added here
    response_data = response.json()
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("Member Portal Details: ", json_str)

    # assert empid_1 == "644576", "empId is not the expected value"
    print(response_data["memberIdSource"])

    EMPID1 = response_data["empId"]
    print("EMP ID IS :" + EMPID1)
    print("emp_payload :" + emp_payload["empId"])

    assert response_data["empId"] == emp_payload["empId"], "empId is not the expected value"

    member_id_source = response_data.get("memberIdSource")
    print("Member ID Source :", member_id_source)
    return member_id_source


def test_getmember(test_fetch_emp_data_with_token):
    get_url = f"https://testfabric.carynhealth.com/api/v31/enrollment/getViewDetails/{test_fetch_emp_data_with_token}"
    print(get_url)
    # Make the GET request
    member_response = requests.get(get_url)
    #print(member_response.text)
    # Check if the request was successful (status code 200)
    assert member_response.status_code == 200, f"GET request failed with status code {member_response.status_code}"
    response_data1 = member_response.json()
    json_data1 = member_response.json()
    json_str1 = json.dumps(json_data1, indent=4)
    print("Member Details: ", json_str1)

    # Extract the Data
    client_name = response_data1["response"]["clientName"]
    email = response_data1["response"]["email"]
    Member_ID = response_data1["response"]["memberId"]
    firstName = response_data1["response"]["firstName"]
    lastName = response_data1["response"]["lastName"]


    print("Client Name:",client_name)
    print("Email ID :",email)
    print("Member ID :",Member_ID)
    print("firstName :",firstName)
    print("lastName :",lastName)
