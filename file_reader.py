### Reading from a text file

with open('pi.txt') as file_object:
    contents = file_object.read()
    print(contents)


with open('pi.txt') as file_object:
    for line in file_object:
        print(line)

with open('pi.txt') as file_object:
    pi_lines = file_object.readlines()

for line in pi_lines:
    print(line.rstrip())
