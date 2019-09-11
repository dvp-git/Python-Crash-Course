# Exerecise 5.10 Checking usernames

# Current user list
current_users = ['service','admin','vplex','conectivity','XIO']

#New user list
new_users = ['xio','unity','vmware','service','vplex']

# Converting to lower case , since the username is case insensitive
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Dear " + str(new_user) +",Please enter new username")
    else:
        print(str(new_user) + " is available")
