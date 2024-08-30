import json
import requests

# Specify the sub_id
sub_id = "1eea1131-634e-4315-82c0-43b6b4f58548"

# Construct the API endpoint with the sub_id
api_url = f"https://dev.fabric.carynhealth.com/api/v13/enrollment/getEnrollmentMember/{sub_id}"

# Make the API call
response = requests.get(api_url)
# ANSI escape code for bold text
BOLD = "\033[1m"
# ANSI escape code for underline text
UNDERLINE = "\033[4m"
# ANSI escape code to reset text formatting
RESET = "\033[0m"


# Check if the API call was successful (status code 200)
if response.status_code == 200:
    # Save the response body to a variable
    json_response = response.json()

    # Specify the question IDs to print responses for
    question_ids_to_print = ["1001", "1002", "1008", "1003", "1004", "1005", "1017", "1016", "1011", "1013", "1015", "1014"]

    # Extract and print "questionID", "questionDesc", and "response" for the specified question IDs, member-wise
    for member in json_response["response"]["members"]:
        print(f"\nMember: {BOLD}{UNDERLINE}{member['firstName']} {member['lastName']}{RESET}")
        for question in member["questions"]:
            if question["questionID"] in question_ids_to_print:
                print(f'  questionID: {question["questionID"]}, questionDesc: {question["questionDesc"]}, response: {BOLD}{question["response"]}{RESET}')
else:
    print(f"API call failed with status code: {response.status_code}")
