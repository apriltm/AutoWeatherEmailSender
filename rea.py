import json

email_list = []

with open('emails.json') as json_data:
    data = json.load(json_data)
    for i in data['emails']:
        email_list.append(i['email'])
