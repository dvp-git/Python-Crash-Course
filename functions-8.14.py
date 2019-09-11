# Exerecise 8.14 Cars


##Defining a function called cars which displpays the information about the car
def car_features(color,manufacturer='toyota',**other):
    """Summarizing the car configurations"""
    car_info = {
        'color':color,
        'manufacturer':manufacturer,
        }
    for key,value in other.items():
        car_info[key] = value
    return car_info

##calling the car

car_1 = car_features('black','mercedes',body='metallic',speed='250kmph')

car_2 = car_features('red','',body='matte',speed='400kmph')
    
print(car_1)

print(car_2)
