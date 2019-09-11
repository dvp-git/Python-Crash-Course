# Exerecise 8.8 User Albums

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
               
while True:
    artist = input("Enter the artist: ")
    if artist == 'quit':
        break
    album = input("Enter the album: ")
    if album == 'quit':
        break
    user_favs = make_album(artist,album)
    print(user_favs) 

