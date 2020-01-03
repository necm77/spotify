# Spotify Toolkit Version 1
# Nick Totman
# Run this from terminal??

import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

# Import saved information to access Spotify API
with open('Account.txt', 'r') as f:
    x = f.read().splitlines()
client_ID = x[5]
client_secret = x[7]
redirect_uri = "http://localhost:8888/callback/"
print('Client ID: ' + client_ID)
print('Client Secret: ' + client_secret)

# Create Token (?) to be able to access Spotify API
client_credentials_manager = SpotifyClientCredentials(client_id=client_ID, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Sign into Spotify
print('Reminder, your password is: ' + x[3])
if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

scope = ''
token = util.prompt_for_user_token(username, scope, client_ID, client_secret, redirect_uri)

if token:
    print('Looks good Nick!')
else:
    print('Fucked it somewhere :(')

# Access my Discover Weekly
