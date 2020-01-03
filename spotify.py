# Spotify Toolkit Version 1
# Nick Totman

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


with open('Account.txt', 'r') as f:
    x = f.read().splitlines()

client_ID = x[5]
client_secret = x[7]

print('Client ID: ' + client_ID)
print('Client Secret: ' + client_secret)

client_credentials_manager = SpotifyClientCredentials(client_id=client_ID, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
