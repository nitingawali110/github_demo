import requests
import random
import json
import string
import pytest

#baseurl;
base_url="https://dev.fabric.carynhealth.com"

sub_id=1689687694939
Transaction_id=8541313220

#auth token

# GET Request for Transaction Receipt
def get_request_Transaction_Receipt():
    url_TR=base_url+"/api/v34/adminportal/sendTransactionReceipt"+"/sub_id/Transaction_id"
    print("get url: " + url_TR)
    response = requests.get(url_TR)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json GET response body: ", json_str)
    print("Email Status:",json_data["response"])
    print(".......GET Transaction Receipt IS Done.......")
    print(".......=====================.......")

# GET Request for Refund Receipt
def get_request_Refund_Receipt():
    url_RR=base_url+"/api/v34/adminportal/sendRefundEmail"+"/sub_id/Transaction_id"
    print("get url: " + url_RR)
    response = requests.get(url_RR)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json GET response body: ", json_str)
    print(".......GET Refund Receipt IS DONE.......")
    print(".......=====================.......")

# GET Request for Send Welcome Email
def get_request_Send_Welcome_Email():
    url_SWE=base_url+"/api/v34/adminportal/sendWelcomeEmail"+"/sub_id"
    print("get url: " + url_SWE)
    response = requests.get(url_SWE)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json GET response body: ", json_str)
    print(".......GET Send Welcome Email IS DONE.......")
    print(".......=====================.......")


#call
get_request_Transaction_Receipt()
get_request_Refund_Receipt()
get_request_Send_Welcome_Email()
