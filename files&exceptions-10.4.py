## Exercise 10.4 Guest Book

###Prompting user for name:

while True:
    user_name = input("Please tell me your name")
    if(user_name == 'quit'):
        break
    else:
        print("Welcome, Mr. ",user_name)
        with open('guest_book.txt','a') as object:
            object.write("\n" + user_name)

    
