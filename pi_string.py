### Files in python

file_name = 'pi_digits.txt'

### Storing the file_name as an object using the open() method
with open(file_name) as file_object:
    
### reading the file to memory
    lines = file_object.readlines()



###Working with  File's content

pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string)
print(len(pi_string))


    
