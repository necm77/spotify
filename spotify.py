# Spotify Toolkit Version 1
# Nick Totman

import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

def main():
    file = import_info('Account.txt')
    username = file[1]
    client_ID = file[5]
    client_secret = file[7]
    redirect_uri = file[9]
    print('Username: ' + username)
    print('Client ID: ' + client_ID)
    print('Client Secret: ' + client_secret)
    print('Redirect URI: ' + redirect_uri)
    token = create_token(file, 'playlist-read-private')
    sp = spotipy.Spotify(auth=token)
    if token:
        print('It Worked!!!')
    else:
        print('Fucked it somewhere :(')
        sys.exit()
    print()
    print('----------------------------------------')
    print()
    print('Welcome to Spotify Tracker')
    discover_tracks = access_playlist(file, sp)
    if not discover_tracks:
        print('Discover Weekly: Not Found')
        sys.exit()
    print_playlist(discover_tracks)


def import_info(text_file):
    # Import saved information to access Spotify API
    with open(text_file, 'r') as f:
        file = f.read().splitlines()
    return file


def create_token(file, scope):
    # Create Token to be able to access Spotify API & Sign into Spotify
    # Authorization Code Flow
    print('Reminder, your password is: ' + file[3])

    token = util.prompt_for_user_token(file[1], scope, file[5], file[7], file[9])
    return token


def access_playlist(file, sp):
    # Access my Discover Weekly
    playlists = sp.user_playlists(file[1])
    for playlist in playlists['items']:
        if playlist['name'] == 'Discover Weekly':
            print(playlist['name'] + ': Found')
            discover = sp.user_playlist(file[1], playlist['id'], fields="tracks,next")
            discover_tracks = discover['tracks']
            return discover_tracks

def print_playlist(playlist):
    for i, item in enumerate(playlist['items']):
        track = item['track']
        print("\t %d %32.32s %s" % (i + 1, track['artists'][0]['name'], track['name']))


main()
