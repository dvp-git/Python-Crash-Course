## Exercise 6.9 Favourite Numbers

favourite_number = {
    'anna':[6,3,2],
    'dan':[8,7,1],
    'amber':[10,99,392],
    'denver':[9],
    'jess':[10,32]
    }

for name,numbers in favourite_number.items():
    print("\n" + name.title() + " 's favourite numbers are:")
    for number in numbers:
        print("\t" + str(number))

        
