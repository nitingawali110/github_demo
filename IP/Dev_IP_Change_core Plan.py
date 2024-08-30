import json
import pytest
import requests

url = "https://dev.fabric.carynhealth.com/api/v33/enrollment/plan/update"

payload = {
    "subId": "46ac0b2c-cac6-4dbd-b7a9-beee283b69ca",
    "planCode": "Elite MD 4",
    "source": "1707908028820",
    "planId": "10034"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.put(url, json=payload, headers=headers)

if response.status_code == 200:
    print("Request successful!")
    # Print the response in a pretty format
    print("Response:")
    print(json.dumps(response.json(), indent=2))
else:
    print(f"Request failed with status code {response.status_code}")
    print("Response:", response.text)
