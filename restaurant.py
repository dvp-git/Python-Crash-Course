## Making a class called Restaurant

class Restaurant():
    """Summarizing what is needed for the restaurant class"""
    def __init__(self, restaurant_name,cuisine_type, served=0):
        """ Saving the attriubutes in the object instance"""
        self.restaurant = restaurant_name
        self.cuisine = cuisine_type
        self.served = served

### Making a method called describe restaurant
    def describe_restaurant(self):
        """Summarizing the 2 pieces of information above"""
        print("\n==========This is our restaurant " + self.restaurant.title() + "===============")
        print("We serve you amazing " + self.cuisine + " 's cusine")

### Making a method called open restaurant
    def open_restaurant(self):
        """Summarizing the time the restaurant is open"""
        print("The restaurant is open now ")

## Printing the number of customers resturant has served
    def set_number_served(self,served):
        """Allow user to set the number of customer's been served"""
        self.served = served
        
## Update the number of customers resturant is serving
    def increment_number_served(self,additional_served):
        """Update the number of customer's that are served"""
        self.served += additional_served
