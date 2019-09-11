## Exercise 6.11 Cities

cities = {
    'Bangalore':{
        'Country':'India',
        'Population':10000000,
        'Fact': 'IT city',
        },
    'Mangalore':{
        'Country':'India',
        'Population':500000,
        'Fact': 'Best food',
        },
    'Manipal':{
        'Country':'India',
        'Population':300000,
        'Fact': 'Good universities',
        }
    }
    

for city,info in cities.items():
    print("\nInformation about " + city.title())
    for heading,explanation in info.items():
        print(heading.title() + " : " + str(explanation))
