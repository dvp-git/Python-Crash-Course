## Exercise 9.2 Three Restaurants

## Making a class called Restaurant

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

### Making threet instance of class Restaurant()
my_restaurant = Restaurant('Plaza','Vietnamese')

your_restaurant = Restaurant('PhoPho','chinese')

our_restaurant = Restaurant('Nus-Ret','all-amercan')



## Describing each of the above 3 restaurants

my_restaurant.describe_restaurant()
your_restaurant.describe_restaurant()
our_restaurant.describe_restaurant()
