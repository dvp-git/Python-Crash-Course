## Exercise 9.7 Admin

## Making a class called User

class User():
    """Making the attruibutes"""
    def __init__(self,
                 first_name,
                 last_name,
                 age,
                 eid
                 ,):
        self.first = first_name
        self.last = last_name
        self.id = eid
        self.age = age

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



## Making a Class called Admin:

class Admin(User):
    """inherit the properties of the parent class User"""
    
    def __init__(self,first_name,last_name,age,eid):
        """Inherit the parent class attributes"""
        super().__init__(first_name,last_name,age,eid)
        self.priveleges = []
        
    def show_priveleges(self):
        """ List the administrators priveleges"""
        print("The following are the priveleges of the admin:")
        for privilege in self.priveleges:
            print("...: " + privilege)


admin_user_1 = Admin('Darryl','Vas',24,1023)
admin_user_1.priveleges=[
                         "can add post",
                         "can delete post",
                         "can ban user",
                         ]

admin_user_1.show_priveleges()
            
