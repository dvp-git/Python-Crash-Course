# Exerecise 5.8 Hello Admin

user_list = ['server','client','admin','service','support']

for user in user_list:
    if (user == 'admin'):
        print("Hello " + user + " Would you like to see the status report?")
    else:
        print("Hello " + user + ",Thank you for logging in again")
