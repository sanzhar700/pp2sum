#Convert from JSON to Python object ---
import json

emp = '{"id":"09", "name": "Nitin", "department":"Finance"}'
print("This is JSON", type(emp))

print("Now convert from JSON to Python")
d = json.loads(emp)
print("Converted to Python", type(d))
print(d)


#Convert from Python object to JSON ---
import json

d = {'id': '09', 'name': 'Nitin', 'department': 'Finance'}
print("This is Python", type(d))

print("Now Convert from Python to JSON")
obj = json.dumps(d, indent=4)
print("Converted to JSON", type(obj))
print(obj)



#parsing data from json into python ---
'''Python JSON to Dictionary
json.loads() function parses a JSON string into a Python dictionary.'''



#parse json ---
import json

geek = '{"Name": "nightfury1", "Languages": ["Python", "C++", "PHP"]}'
geek_dict = json.loads(geek)

# Displaying dictionary
print("Dictionary after parsing:", geek_dict)
print("\nValues in Languages:", geek_dict['Languages'])

#Python JSON to Ordered Dictionary ---
import json
from collections import OrderedDict

data = json.loads('{"GeeksforGeeks":1, "Gulshan": 2, "nightfury_1": 3, "Geek": 4}', 
                  object_pairs_hook=OrderedDict)
print("Ordered Dictionary: ", data)



#Parse using JSON file ---
import json

with open('data json') as f:
    data json.load(f)

#printing data from json file
print(data)