from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import webbrowser
import pyautogui
from time import sleep

# Autenticación
client_id = "195351508b814052ae1b1685ef8fcacd"
client_secret = "c3bfe7eb9d76420d88cac90b3134e471"

flag = 0
autor = 'dj tiesto' 
# song = "del mar ozuna".upper()
song = "the bussines".upper()


if len(autor) > 0:

    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
    result = sp.search(autor)

    for i in range(0, len(result["tracks"]["items"])):
        name_song = result["tracks"]["items"][i]["name"].upper()
        if song in name_song:
            flag = 1
            webbrowser.open(result["tracks"]["items"][i]["uri"])
            sleep(5)
            pyautogui.press("enter")

if flag == 0:
    song= song.replace(" ", "%20")
    webbrowser.open(f'spotify:search:{song}')
    sleep(5)
    pyautogui.press("enter")

    for i in range(4):
        pyautogui.press("tab")  
    pyautogui.press("enter")

