# This is a simple script to build txt file whit a list of user information from Lupe
import requests
import json

f = open('in.json')
data = json.load(f)
result = []

for index, user in enumerate(data['users']):
    response = requests.get(
      "https://services.mxgrability.rappi.com/lupe/grability/api/users/"+
      str(user)+"?churnRisk=true&referredCoupons=true&segment=true&hvuData=true",
      headers=data['headers']).json()
    result.append({
        "USERID": user,
        "EMAIL": response['data']['email'],
        "PHONE": response['data']['phone']
    })
    print(index)
print(result)
