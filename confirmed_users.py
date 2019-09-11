##confirmed_users.py

#Start with users that need to be verified, and an empty list to hold confirmed users

unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

while unconfirmed_users != [] :
    current_user = unconfirmed_users.pop()

    print("Verifying user:" + current_user.title())
    confirmed_users.append(current_user)

## Displaying all the confirmed users
print("\n The following users have been confirmed:")
for users in confirmed_users:
    print(users)
    
