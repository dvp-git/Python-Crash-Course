# Exerecise 8.10 Great Magicians


##Defining a function called show_magicians
def show_magicians(magicians):
    for key in magicians:
        print("Hello " + key)



## Defining a fucntion called make_great
def make_great(magicians):
    """Add 'the Great' to each magicians name"""
    ### Building a list to store the great magicians
    great_magicians = []

    ##Making each magician great, and adding it to great_magician's list
    while magicians:
        current_magician = magicians.pop()
        great_magician = current_magician + ' the Great'
        great_magicians.append(great_magician)

    ### Again storing the great_magicians back in the original magicians list
    for great_magician in great_magicians:
        magicians.append(great_magician)
        
        
## List of magicians names
magicians = ['zorro','criss','david','street','gambit']



show_magicians(magicians)

make_great(magicians)


show_magicians(magicians)
