## Exercise 9.5 Login Attempts

## Making a class called User

class User():
    """Making the attruibutes"""
    def __init__(self,
                 first_name,
                 last_name,
                 age,
                 eid
                 ):
        self.first = first_name
        self.last = last_name
        self.id = eid
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """Printing the summary of the user"""
        print("==========User Profile: " + str(self.id) + "==========")
        print("First name : " + self.first.title())
        print("Last name : " + self.last.title())
        print("Employee age: " + str(self.age))
        print("Employee ID: " + str(self.id))

    def greet_user(self):
        """Printing the greeting for the user"""
        print("\n=============Welcome Mr./Ms. " + self.first.title() + "===================")
        print("Welcome to this simulation")
        print("You are player" + str(self.id))

    def increment_login_attempts(self):
        """Increase the counter of login attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """ Reset the login attempts"""
        self.login_attempts = 0
      


## Create user Darryl
        
darryl = User('Darryl','Prabhu',23,1096362)

darryl.describe_user()
darryl.greet_user()

## Make 2 attempts
darryl.increment_login_attempts()
darryl.increment_login_attempts()

print("Login attempts: " + str(darryl.login_attempts))

darryl.reset_login_attempts()

print("Login attempts: " + str(darryl.login_attempts))

