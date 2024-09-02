import requests
import random
import json
import string
import pytest

# base URL
base_url="https://testfabric.carynhealth.com/"
sub_id="b8befd84-a0d0-426b-9c57-5f0c41784bfb"

#headres
headers= {
        "Content-Type": "application/json"
        }

# GET Request for Medical Questions
def test_medicalQuestions():
    url_medical=base_url+"api/v33/enrollment/getEnrollmentMember/b8befd84-a0d0-426b-9c57-5f0c41784bfb"
    print("get url: " + url_medical)
    response = requests.get(url_medical,headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    # json_str = json.dumps(json_data, indent=4)
    # print("json Medical Questions Data: ", json_str)
    data = response.json()

# Extract and print questions data
    questions = data["response"]["members"][0]["questions"]
    json_str = json.dumps(questions, indent=4)
    print("Medical Questions Data:", json_str)
    # print("Question Description:", questions["questionDesc"])
    # print("Response:", questions["response"])


# Extract the question ID for the member
    question_0 = data["response"]["members"][0]["questions"][0]["questionID"]
    question_1 = data["response"]["members"][0]["questions"][1]["questionID"]
    question_2 = data["response"]["members"][0]["questions"][2]["questionID"]
    question_3 = data["response"]["members"][0]["questions"][3]["questionID"]
    question_4 = data["response"]["members"][0]["questions"][4]["questionID"]
    question_5 = data["response"]["members"][0]["questions"][5]["questionID"]

# Assert that the question ID is equal to "1001"-"1006"
    assert question_0 == "1001" ,"Assertion Failed: Question ID 1001 not present "
    assert question_1 == "1002" ,"Assertion Failed: Question ID 1002 not present "
    assert question_2 == "1003" ,"Assertion Failed: Question ID 1003 not present "
    assert question_3 == "1004" ,"Assertion Failed: Question ID 1004 not present "
    assert question_4 == "1005" ,"Assertion Failed: Question ID 1005 not present "
    assert question_5 == "1006" ,"Assertion Failed: Question ID 1006 not present "

# Print a message if the assertion passes
    print("Assertion passed: Question ID is 1001")
    print("Assertion passed: Question ID is 1002")
    print("Assertion passed: Question ID is 1003")
    print("Assertion passed: Question ID is 1004")
    print("Assertion passed: Question ID is 1005")
    print("Assertion passed: Question ID is 1006")


# Extract the response for Question ID 1006 for the member
    response_1 = data["response"]["members"][0]["questions"][0]["response"]
    response_2 = data["response"]["members"][0]["questions"][1]["response"]
    response_3 = data["response"]["members"][0]["questions"][2]["response"]
    response_4 = data["response"]["members"][0]["questions"][3]["response"]
    response_5 = data["response"]["members"][0]["questions"][4]["response"]
    response_6 = data["response"]["members"][0]["questions"][5]["response"]

# Print the Question Response
    print("Question 1 Response:",response_1)
    print("Question 2 Response:",response_2)
    print("Question 3 Response:",response_3)
    print("Question 4 Response:",response_4)
    print("Question 5 Response:",response_5)
    print("Question 6 Response:",response_6)

#x.response.members[0].questions[5].response

# Assert that the response is equal to "Food Service"
    assert response_6 == "Food Service"

# Print a message if the assertion passes
    print("Assertion passed: Response for Question ID 1006 is 'Food Service'")




test_medicalQuestions()

