# Exerecise 8.11 Unchanged Magicians


##Defining a function called show_magicians
def show_magicians(magicians):
    for magician in magicians:
        print("Hello " + magician)



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
    return great_magicians

    ### Again storing the great_magicians back in the original magicians list
    ###for great_magician in great_magicians:
    ###    magicians.append(great_magician)
        
       
        
## List of magicians names
magicians = ['zorro','criss','david','street','gambit']
show_magicians(magicians)

###Copy of the magician list which was modified
print("\nGreat magicians")
unchanged_magician = make_great(magicians[:])
show_magicians(unchanged_magician)

### Unchanged magician list
print("\nUnchanged list")
show_magicians(magicians)
