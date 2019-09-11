## Exercise 5.2 More Conditional Tests

name_1 = "Darryl"
name_2 = "Darrly"
name_3 = "Darryl"

#Equality of strings

if (name_1 == name_3):
    print("Equal!")
else:
    print("Unequal!")

# Inequality of strings

if(name_1 != name_2):
    print("The names are unequal")
else:
    print("The names are equal")

# Numerical tests

age_1 = 18

age_2 = 23

if (age_1 ==18):
    print("Person is eligible to vote")

if(age_1 != 23):
          print("Person cannot drink")

if(age_1 <= age_2):
    print("Yonger")

if(age_2 >= age_1):
    print("Older")

# and/or keyword test
if (age_1 ==18 or age_23>=23):
    print("Person is eligible for voting")

if(age_1 ==18 and age_2==23):
    print("Age difference is 5 years")

## Item in list or not
fruits = ['apple','peach','melon']
if 'apple' in fruits:
    print("Apple is present in fruits")
if 'guava' not in fruits:
    print("Guava is not present in fruits")
