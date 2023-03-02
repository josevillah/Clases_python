from cgitb import text
from email.mime import audio


import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser


from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

import pyautogui
from time import sleep



# escuchar nuestro microfono y devolver el audio como texto
def verificarExiste():
	if 'sp' in globals():
		return True
	else:
		return False


def menu():
    saludo()
    inicio = True
    while inicio:
        texto = audio_a_texto().lower()
        if 'alfa' in texto:
            texto = texto.replace('alfa', '')
            # if 'abre youtube' in texto:
            #     hablar('Abriendo Youtube', helena)
            #     webbrowser.open('http://www.youtube.com')
            #     continue

            elif 'abre el navegador' in texto:
                hablar('Abriendo el Navegador', helena)
                webbrowser.open('http://www.google.com')
                continue

            # elif 'qué hora es' in texto:
            #     hora()
            #     continue

            # elif 'qué día es hoy' in texto:
            #     dia()
            #     continue

            # elif 'qué es' in texto:
            #     hablar('Buscando en Wikipedia', helena)
            #     wikipedia.set_lang('es')
            #     respuesta = wikipedia.summary(texto, sentences=1)
            #     hablar(f'Según Wikipedia:', helena)
            #     hablar(respuesta, helena)
            #     continue

            elif 'quién es' in texto:
                hablar('Buscando en Wikipedia', helena)
                wikipedia.set_lang('es')
                respuesta = wikipedia.summary(texto, sentences=1)
                hablar(f'Según Wikipedia:', helena)
                hablar(respuesta, helena)
                continue

            elif 'busca en internet' in texto:
                hablar('Ejecutando el Navegador', helena)
                texto = texto.replace('busca en internet', '')
                pywhatkit.search(texto)
                hablar('Esto es lo que he encontrado', helena)
                continue

            # elif 'reproduce en youtube' in texto:
            #     hablar('Reproduciendo en Youtube', helena)
            #     texto = texto.replace('reproduce en youtube', '')
            #     pywhatkit.playonyt(texto)
            #     continue
            
            elif 'reproduce' in texto:
                texto = texto.replace('reproduce', '')
                hablar('Reproduciendo en Spotify '+texto, helena)
                result = verificarExiste()
                if len(musica) == 0:
                    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
                    result = sp.search(texto)
                    webbrowser.open(result["tracks"]["items"][0]["uri"])
                    musica.append(True)
                else:
                    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
                    result = sp.search(texto)
                    webbrowser.open(result["tracks"]["items"][0]["uri"])
                    sleep(3)
                    pyautogui.press("enter")
                continue

            elif 'dime un chiste' in texto or 'cuenta me un chiste' in texto:
                hablar(pyjokes.get_joke('es'), helena)
                continue
            elif 'precio de las acciones' in texto:
                accion = texto.split('de')[-1].strip()
                cartera = {
                    'apple': 'APPL',
                    'amazon': 'AMZN',
                    'google': 'GOOGL'
                }
                try:
                    buscar = cartera[accion]
                    buscar = yf.ticker(buscar)
                    precio = accion.info['regularMarketPrice']
                    hablar(f'El precio de {accion} es {precio}')
                    continue
                except:
                    hablar('No he conseguido el precio de {accion}')
            elif 'me voy' in texto:
                hablar('Que te vaya bien. Hasta pronto', helena)
                break
            continue

menu()