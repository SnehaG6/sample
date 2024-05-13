import json

person = '{"name": "Sneha", "languages": ["English", "Malayalam"]}'
person_dict = json.loads(person)

print( person_dict)

print(person_dict['languages'])