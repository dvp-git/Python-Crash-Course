## Exercise 7.10 Dream Vacation

polling_active = True

## Visiting one place in the world from multiple users
user_dreams = {}



while polling_active:
    user = input("Please introduce youreself")
    dream = input("Could you tell us your dream in life? ")
    
## Stroring the users as keys and dreams as values in the dictionary user_dreams
    user_dreams[user] = dream

    repeat = input("Would we like to stop the poll here")

    if repeat == 'yes':
        polling_active = False

## Printing the results of the poll

print("-------Dream responses for each individual--------")
for user,dream in user_dreams.items():
    print("Hi! My name is " + user.title() + " and my dream is to become a " + dream.upper()) 
