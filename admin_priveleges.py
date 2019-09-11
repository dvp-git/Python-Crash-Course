## Making a Class called Admin:

from user import User

class Admin(User):
    """inherit the properties of the parent class User"""
    
    def __init__(self,first_name,last_name,age,eid):
        """Inherit the parent class attributes"""
        super().__init__(first_name,last_name,age,eid)
        self.privileges = Privileges()

## Making a class called Privileges

class Privileges():
    """Making a class called privileges"""
    def __init__(self,privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        """ List the administrators priveleges"""
        print("The following are the priveleges of the admin:")
        for privilege in self.privileges:
            print("...: " + privilege)

