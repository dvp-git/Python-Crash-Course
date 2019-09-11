## Exercise 7.5 Movie Tickets

prompt = ("Welcome! Please tell me your age")

while True:
    age = input(prompt)
    if age == 'quit':
        break
    if int(age) < 3:
        print("You get a free ticket")
    elif int(age)>=3 and int(age)<=12:
        print("Your ticket is $10")
    else:
        print("your ticket is $12")

        
        
