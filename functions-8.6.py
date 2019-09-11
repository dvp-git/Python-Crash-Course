# Exerecise 8.6 City Names

##Defining a function called city

def city_country(city_name,country_name='Iceland'):
     return city_name.title() + ',' + country_name.title()
    

past = city_country('bangalore','India')
print("I used to live in" + ' ' + past)

present = city_country('venice')
print("Now I live in" + ' ' + present)

future= city_country('zurik','Russia')
print("I plan to live in" + ' ' + future)

    
