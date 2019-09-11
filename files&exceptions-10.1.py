## Exercise 10.1 Learning Python

file_name = "learning_python.txt"

print('\n====Reading content by entire file====')
### Reading the file by keeping it open
with open(file_name) as file_object:
    content = file_object.read()
print(content)

print('\n====Reading content by looping over lines====')
### Reading the file by looping over the fileobject
with open(file_name) as file_object:
    for line in file_object:
        print(line.strip())

print("\n====Reading content by using the loop outside 'with' block====")
###Reading the file by looping over the file object outside the file
with open(file_name) as file_object:
    lines = file_object.readlines()

###Looping outside the with block after storing as a list 'lines'
for line in lines:
    print(line.rstrip())
