# Exerecise 5.9 No Users

#user_list = ['server','client','admin','service','support']

user_list = []

if user_list:
    for user in user_list:
        if (user == 'admin'):
            print("Hello admin, Would you like to see the status report?")
        else:
            print("Hello " + str(user) + ",Thank you for logging in again")
else:
    print("We need to find some users")


        
