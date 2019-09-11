### Storing data in JSON

import json

numbers = [1, 2, 3, 5, 7, 9, 13]

filename = 'numbers.json'
with open(filename,'w') as file_obj:
    ### Using the JSON dump fundtion to storage the nmumbers in JSON
    json.dump(numbers,file_obj)


    
