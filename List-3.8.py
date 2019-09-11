#Exercise 3.8

places = ['Paris','Brazil','New york','Sydney','Las Vegas']

print(places)

## Printing sorted
print("Printing sorted List:" + str((sorted(places))))

##Printing original
print("Original List:" + str(places))

##Printing reverse sorted
print("Printing Reversed alphabetical list:" + str(sorted(places,reverse=True)))


##Printing original
print("Original List:" + str(places))

##Reverse list
places.reverse()
print("Reverse List:" + str(places))

##Reverse list will show original
places.reverse()
print("Reverse List again to show original:" + str(places))

##Sorting alphabetically 
places.sort()
print("Sorted List alphabetically permanently" + str(places))

##Reverse alphabetical order
places.sort(reverse=True)

print("Sorting list in reverse alphabetical order" + str(places))
