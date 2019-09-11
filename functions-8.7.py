# Exerecise 8.7 Album

##Defining a function called make_album

def make_album(artist_name,album_name,track_numbers=15):
    """ Making an album to store artist name and album name"""
    album_1 = {
        'artist':artist_name,
        'album':album_name,
        }
    if track_numbers:
        album_1['tracks'] = track_numbers
    return album_1
               

oldies = make_album('GNR','Patience',32)
print(oldies) 

present = make_album('IRON MAIDEN','Fear',22)
print(present) 

future= make_album('DEF LEPPARD','Photograph')
print(future) 
    
