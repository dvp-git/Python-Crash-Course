### Loading data in JSON

import json

filename = 'numbers.json'
with open(filename) as file_obj:
    ### Using the JSON load fundtion to load the nmumbers from a JSON file
    numbers = json.load(file_obj)

print(numbers)

    
