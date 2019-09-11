# Exerecise 8.3 T-Shirt

##Defining a function called t-shirt
def make_shirt(logo,size=32,):
 ##   shirt_size = int(input("Select the size of the t-shirt you require"))
##    logo = input("Enter the logo")
    """Summary of the selected size and logo"""
    print("======Shirt ready=========")
    print("T-Shirt " + logo.title() + " of size " + str(size) + " is ready")

## Using positional arguments

make_shirt("Beat the heat",42)


## Using keyword argument

make_shirt(logo='Code repeat!',size=40)

           
## Using default

make_shirt('Define Success')
