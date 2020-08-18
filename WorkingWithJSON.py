import json

person_dict = {'first': 'Ahmed', 'last': 'Ade;'}

person_dict['City'] = "Suez"

person_json = json.dumps(person_dict)

print(person_json)