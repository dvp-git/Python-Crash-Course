## Exercise 6.8 Pets

## Make an empty list called people

pets = []

## Making 3 dictionary with different characteristics:

pet = {
    'animal type': 'dog',
    'name': 'coco',
    'owner': 'Darryl',
    'weight': 43,
    'eats': 'bones',
    }

pets.append(pet)

pet = {
    'animal type': 'cat',
    'name': 'fluffy',
    'owner': 'Jen',
    'weight': 35,
    'eats': 'fish',
    }

pets.append(pet)

pet = {
    'animal type': 'turtle',
    'name': 'merv',
    'owner': 'Alex',
    'weight': 20,
    'eats': 'grass',
    }
pets.append(pet)

#Display information about each pet

for pet_info in pets:
    print("\nName:" + pet_info['name'].title())
    for key,value in pet_info.items():
        if value == pet_info['name']:
            continue
        print(key.title()+ ":" + str(value))
