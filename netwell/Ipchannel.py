import requests

url = "https://dev.fabric.carynhealth.com/api/v33/enrollment/channelUpForIP"

# Test Case: Valid Request
valid_payload = {
    "clientId": 3042,
    "clientName": "Test Nitin 3042",
    "programNames": ["Elite-MD", "Optimum-MD"],
    "addonNames": ["Essential", "Guardian", "Dental"]
}
response = requests.post(url, json=valid_payload)
print("Valid Request:", response.status_code, response.json())

# Test Case: Missing clientId
missing_client_id_payload = {
    "clientName": "Guided Hand",
    "programNames": ["Elite-MD", "Optimum-MD"],
    "addonNames": ["Essential", "Guardian", "Dental"]
}
response = requests.post(url, json=missing_client_id_payload)
print("Missing clientId:", response.status_code, response.json())

# Test Case: Invalid Data Type for clientId
invalid_client_id_payload = {
    "clientId": "invalid_id",
    "clientName": "Guided Hand",
    "programNames": ["Elite-MD", "Optimum-MD"],
    "addonNames": ["Essential", "Guardian", "Dental"]
}
response = requests.post(url, json=invalid_client_id_payload)
print("Invalid clientId:", response.status_code, response.json())

# Add more test cases similarly...
