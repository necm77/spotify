# Spotify Toolkit Version 1
# Nick Totman

import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

# Import saved information to access Spotify API
with open('Account.txt', 'r') as f:
    x = f.read().splitlines()
username = x[1]
client_ID = x[5]
client_secret = x[7]
redirect_uri = x[9]
print('Username: ' + username)
print('Client ID: ' + client_ID)
print('Client Secret: ' + client_secret)
print('Redirect URI: ' + redirect_uri)

# Create Token (?) to be able to access Spotify API & Sign into Spotify
# Authorization Code Flow
print('Reminder, your password is: ' + x[3])
scope = 'playlist-read-private'

token = util.prompt_for_user_token(username, scope, client_ID, client_secret, redirect_uri)
sp = spotipy.Spotify(auth=token)
if token:
    print('Looks good Nick!')
else:
    print('Fucked it somewhere :(')

# Access my Discover Weekly
