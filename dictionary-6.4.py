# Exerecise 6.5 Rivers

rivers = {'Ganga':'India','Nile':'Egypt','Amazon':'USA'}

#Loop for each river
for river,country in rivers.items():
    print(river.title() + " runs through " + country.title())

#Loop for each river present
for river in set(rivers.keys()):
    print("Rivers here:" + river.title())

#Loop for each country
for river in (rivers.values()):
    print("Country's listed:" + river.title())

    

    

        
        
        
