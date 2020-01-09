# Spotify Toolkit Version 1
# Nick Totman

import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import json

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
    # discover_tracks = access_playlist(file, 'New', sp)
    discover_tracks = access_playlist(file, 'Discover Weekly', sp)
    if not discover_tracks:
        print('Discover Weekly: Not Found')
        sys.exit()
    # print(json.dumps(discover_tracks, indent=4))
    print_playlist(discover_tracks)
    disc = access_playlist(file, 'Discover', sp)
    if not disc:
        print('Discover: Not Found')
        sys.exit()
    # print(json.dumps(disc, indent=4))
    print_playlist(disc)


def import_info(text_file):
    # Import saved information to access Spotify API
    with open(text_file, 'r') as f:
        file = f.read().splitlines()
    return file


def create_token(file, scope):
    # Create Token to be able to access Spotify API & Sign into Spotify
    # Authorization Code Flow
    print('Reminder, your password is: ' + "*" * (len(file[3]) - 4) + file[3][-4:])  # Only prints last 4 digits

    token = util.prompt_for_user_token(file[1], scope, file[5], file[7], file[9])
    return token


def access_playlist(file, name, sp):
    # Access my Discover Weekly
    playlists = sp.user_playlists(file[1])
    for playlist in playlists['items']:
        if playlist['name'] == name:
            print(playlist['name'] + ': Found')
            discover = sp.user_playlist(file[1], playlist['id'], fields="tracks,next")
            discover = discover['tracks']
            nextsong = discover
            discover = discover['items']
            while nextsong['next']:
                nextsong.update(sp.next(nextsong))
                discover.extend(nextsong['items'])
            return discover

def print_playlist(playlist):
    for i, item in enumerate(playlist):
        print("\t %d %32.32s : %s" % (i + 1, playlist[i]['track']['artists'][0]['name'], playlist[i]['track']['name']))


main()
