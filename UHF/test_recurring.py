import requests

# Get user input for sub_id
sub_id = "5133f2c2-8b1f-4bac-abb1-0c9813d385e1"

# URL and payload data
url = f"https://dev.fabric.carynhealth.com/aecpaymentService/api/v1/schedulePayment/{sub_id}"
payload = {}

# Making the POST request
response = requests.post(url, json=payload)

# Checking the response
if response.status_code == 200:
    print("POST request successful!")
    print("Response:", response.json())
else:
    print("POST request failed!")
    print("Status code:", response.status_code)
