prompt_name = "Hi! Please tell me your name"
prompt_response = "Do you like the food here?"

## Empty dictionary to store the responses of the user in a dictionary
responses = {}

##Setting a flag that pollig is active
polling_active = True

while polling_active:
    user = input(prompt_name)
    response = input(prompt_response)
    
##Storing the value of user and response in a dictionary
    responses[user] = response

    repeat = input("Would you like another person to vote? ")
    if repeat == 'no':
        polling_active = False

##Displaying the result of the poll
print("\n-----Poll results------")
for user,response in responses.items():
    print(user.title() + " voted " + response)
