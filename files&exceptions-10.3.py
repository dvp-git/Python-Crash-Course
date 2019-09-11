## Exercise 10.3 Guest

###Prompting user for name:

user_name = input("Please tell me your name")

with open('guest.txt','w') as object:
    object.write(user_name)

    
