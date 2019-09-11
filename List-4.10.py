## Exercise 4.10 Slices

names = ['charles', 'martina', 'michael', 'florence', 'eli']

print("The first three items in the list are: ")
for name in names[:3]:
    print(name.title())


print("The first three items in the list are: ")
for middle in names[1:-1]:
    print(middle.title())


print("The last three items in the list are: ")
for last in names[-3:]:
    print(last.title())
