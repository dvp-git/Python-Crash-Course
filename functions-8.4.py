# Exerecise 8.4 Large T-Shirts

##Defining a function called large t-shirt with default arguments
def make_shirt(logo="'I love Python'",size='large'):

    """Summary of the selected size and logo"""
    print("======Shirt ready=========")
    print("T-Shirt " + logo.title() + " of size " + str(size) + " is ready")

## Using positional arguments

make_shirt()


## Using keyword argument

make_shirt(size='medium')

           
## Using default

make_shirt("'Define Success'",'small')
