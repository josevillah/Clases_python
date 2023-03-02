import webbrowser
import pywhatkit


class MyYouTube:

    def __init__(self):
        pass
    
    def openYoutube(self):
        webbrowser.open('http://www.youtube.com')
    
    def play(self, texto):
        pywhatkit.playonyt(texto)