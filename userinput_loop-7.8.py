## Exercise 7.8 Deli

## Making a list called sandwich_orders

sandwich_orders = ['tuna','salami','chicken','beef','bacon','veg','cheese']

finished_sandwiches = []


while sandwich_orders:

    current_sandwich = sandwich_orders.pop()           ## storing the value in a temp variable
    print("I made you a " + current_sandwich + ".")    ## printing the sandwich that was made

    finished_sandwiches.append(current_sandwich)       ## adding the finished sandwich to the finished_sandwich's list

    
print("These sandwiches were made by me!")
for sandwiches in finished_sandwiches:
    print(sandwiches)


    
    


        
        
