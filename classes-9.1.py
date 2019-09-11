## Exercise 9.1 Restaurant

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

### Making an instance of class Restaurant()
my_restaurant = Restaurant('Plaza','Vietnamese')

print(my_restaurant.restaurant)
print(my_restaurant.cuisine)



my_restaurant.describe_restaurant()

my_restaurant.open_restaurant()


    
