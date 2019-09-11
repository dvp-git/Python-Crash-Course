## Exercise 5.6 Stages of life

print(" Stagaes of a man's life")

#Input from keyboard
age = int(input("Enter the person's age"))

if age<2 :
    print("Person is a baby")
elif age>=2 and age<4:
    print("Person is a toddler")
elif age>=4 and age<13:
    print("Person is a kid")
elif age>=13 and age<20:
    print("Person is a teenager")
elif age>=20 and age<65:
    print("Person is an adult")
elif age>65:
    print("Person is an elder")

print("Have a good day")
