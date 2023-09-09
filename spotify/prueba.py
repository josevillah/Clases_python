from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import webbrowser
import pyautogui
from time import sleep

# Autenticación
client_id = "195351508b814052ae1b1685ef8fcacd"
client_secret = "c3bfe7eb9d76420d88cac90b3134e471"
autor = 'daddy yankee'.upper()
song = 'la gasolina'.upper()
songs = []

if len(autor) > 0:
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
    if len(song) == 0:
        result = sp.search(autor)
        name_song = result["tracks"]["items"][0]['name']
        webbrowser.open(result["tracks"]["items"][0]["uri"])
    elif len(song) > 0:
        result = sp.search(song+' '+autor)
        for i in range(0, len(result["tracks"]["items"])):
            songs.append(result["tracks"]["items"][i])
        
        webbrowser.open(songs[0]['uri'])
else:
    if len(song) > 0:
        sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
        result = sp.search(song)
        for i in range(0, len(result["tracks"]["items"])):
            songs.append(result["tracks"]["items"][i])
        
        webbrowser.open(songs[0]['uri'])
