## Exercise 9.6 Ice Cream Stand


## Class called restaurant:

class Restaurant():
    """Summarizing what is needed for the restaurant class"""
    def __init__(self, restaurant_name,cuisine_type):
        """ Saving the attriubutes in the object instance"""
        self.restaurant = restaurant_name
        self.cuisine = cuisine_type

### Making a method called describe restaurant
    def describe_restaurant(self):
        """Summarizing the 2 pieces of information above"""
        print("\n==========This is our restaurant " + self.restaurant.title() + "===============")
        print("We serve you amazing " + self.cuisine + " 's cusine")

### Making a method called open restaurant
    def open_restaurant(self):
        """Summarizing the time the restaurant is open"""
        print("The restaurant is open now ")


## Making a class called Ice_Cream_Stand
class IceCreamStand(Restaurant):
    """A simple class called ice-cream"""
    def __init__(self,restaurant_name,cuisine_type='ice-cream'):
        """initialize the attributes of an ice-cream"""
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = []
    def display_flavors(self):
        """Display the flavors available"""
        print("We have the following flavors""")
        for flavor in self.flavors:
            print(" ..." + str(flavor.title()))

my_ice_cream = IceCreamStand('The Izzys')
my_ice_cream.flavors = ['vanilla','mango','chocolate','butterscotch']

my_ice_cream.describe_restaurant()
my_ice_cream.display_flavors()
    

