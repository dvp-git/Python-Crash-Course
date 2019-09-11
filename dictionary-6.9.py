## Exercise 6.9 Favourite Places

## Make a dictionary called favourite_places

favourite_places = {
    'Darryl':['NY','Paris','Canada'],
    'Nishanth':['UK','France'],
    'Nandish':['Srilanka','UAE','Ireland']
    }


## Looping through the dictionary favourite_places to print each one's selection

for name,places in favourite_places.items():
    print("\n" + name.title() + " 's favourite places are:" )
    for place in places:
        print(place)

        
