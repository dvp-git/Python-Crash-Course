## Exercise 10.5 Programming Poll

###Prompting user for name:


while True:
    feedback = input("Why do you like programming")

    with open('feedback.txt','a') as object:
            object.write("\n" + feedback)

    
