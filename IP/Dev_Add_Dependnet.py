import json
import pytest
import requests

def update_dependents():
    url = "https://dev.fabric.carynhealth.com/api/v33/enrollment/dependents/update"
    payload = {
        "addMembers": [
            {
                "id": None,
                "subId": "9a915e23-079c-4216-b073-f81e0b2a171b",
                "firstName": "New",
                "lastName": "Test",
                "gender": "MALE",
                "relationshipCode": "CHILD",
                "birthDate": "2010-02-02"
            }
        ],
        "removeMembers": [],
        "subId": "9a915e23-079c-4216-b073-f81e0b2a171b",
        "planCode": "Elite MD 2",
        "source": "1707372208418"
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.put(url, json=payload, headers=headers)

    if response.status_code == 200:
        print("Request successful!")
        # Print the response in a pretty format
        print("\nResponse:")
        print(json.dumps(response.json(), indent=2))
    else:
        print(f"Request failed with status code {response.status_code}")
        print("Response:", response.text)

# Run the function
update_dependents()
