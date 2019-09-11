# Exerecise 6.6 Polling

favourite_languages = {'jen':'python','sarah':'C','edward':'ruby','phil':'python'}

#List of people who should take the poll
people_list = ['darryl','dan','jen','phil','mike']

#Loop for each river present
for name in people_list:
    if name in favourite_languages.keys():
        print("Thanks for  voting",name.title())
    else:
        print("Please take the vote",name)
