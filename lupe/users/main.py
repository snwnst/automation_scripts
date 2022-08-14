# This is a simple script to build txt file whit a list of user information from Lupe
import requests
import json
import csv

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
fieldnames = ['USERID', 'EMAIL', 'PHONE']
with open('utput.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerows(result)
