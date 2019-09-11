## Exercise 10.7 Addition Calculator

###Prompting user for 2 numbers:


print("We're gonna calculate the sum of 2 numbers")

print("Enter 'q' to quit")
while True:

    
    try:
        first_number = input("Enter the first number") ### Since the input accepts only string values
        if first_number == 'q':
            break
        first_number = int(first_number)               ### Convert it to an integer value, numbers will convert
        
        second_number = input("Enter the second number")
        if second_number == 'q':
            break
        second_number = int(second_number)             ## If attempting string --> int, it will result in a ValueError
        
    except ValueError:
        print("Enter a valid numeric value only")
        
        
    else:
        sum = first_number + second_number
        print("The sum of " + str(first_number) + " and " + str(second_number) + " = " + str(sum))

        
    
