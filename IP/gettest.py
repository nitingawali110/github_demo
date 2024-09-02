import requests
import random
import json
import string


resp=requests.get("https://reqres.in/api/users?page=2")
code=resp.status_code
json_data=resp.json()

#Validate Response
assert code==200, "Status Code doest Match"
json_str = json.dumps(json_data, indent=4)
# print("json GET response body: ", json_str)
print("Total:",json_data['total'])
print("Total Pages:",json_data['total_pages'])

assert json_data['total']==12,"total is different"
assert json_data['total_pages']==2,"total pages count not match"
print("Employer Email:",json_data["data"][0]["email"])

assert (json_data["data"][0]["email"]).endswith("reqres.in"), "email format is not matching"

print("Employer Email:",json_data["data"][1]["last_name"])





#print(resp.json())
#print(resp.headers)
#print(resp.cookies)
#print(resp.url)




#print(resp.headers)


# print(resp)
# print(dir(resp))
# print(type(resp))
# print(resp.text)

#print(resp.content)
