from cgitb import text
from email.mime import audio
import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import webbrowser
import pyautogui
from time import sleep

sabina = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
helena = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'

client_id = "195351508b814052ae1b1685ef8fcacd"
client_secret = "c3bfe7eb9d76420d88cac90b3134e471"
musica = []

# escuchar nuestro microfono y devolver el audio como texto

def audio_a_texto():
    r = sr.Recognizer()
    with sr.Microphone() as origen:
        r.pause_threshold = 0.5
        print('Habla!!')

        audio = r.listen(origen)
        try:
            texto = r.recognize_google(audio, language='es-ve')

            # Probando el micro
            print('dijiste... ' + texto)
            return texto
        except sr.UnknownValueError:
            print('No entendio lo que dijiste')
            return 'Vuelve a intentarlo...'

        except sr.RequestError:
            print('No entendio lo que dijiste')
            return 'No hay servicio'

        except:
            print('No entendio lo que dijiste')
            return 'Error Desconicido!'


def hablar(mensaje, voz):
    engine = pyttsx3.init()
    engine.setProperty('voice', voz)
    engine.setProperty('rate', 160)
    engine.say(mensaje)
    engine.runAndWait()


def dia():
    fecha = datetime.date.today()
    dia = fecha.weekday()

    calendario = {
        0: 'Lunes',
        1: 'Martes',
        2: 'Miércoles ',
        3: 'Jueves',
        4: 'Viernes',
        5: 'Sábado',
        6: 'Domingo'
    }

    hablar(f'Hoy es {calendario[dia]}', helena)


def hora():
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos.'

    hablar(hora, helena)


def saludo():
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif hora.hour >= 6 and hora.hour < 12:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'

    mensaje = f'{momento}, Soy Alfa, tu asistente virtual. En que te puedo ayudar'
    hablar(mensaje, helena)

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
            if 'abre youtube' in texto:
                hablar('Abriendo Youtube', helena)
                webbrowser.open('http://www.youtube.com')
                continue

            elif 'abre el navegador' in texto:
                hablar('Abriendo el Navegador', helena)
                webbrowser.open('http://www.google.com')
                continue

            elif 'qué hora es' in texto:
                hora()
                continue

            elif 'qué día es hoy' in texto:
                dia()
                continue

            elif 'qué es' in texto:
                hablar('Buscando en Wikipedia', helena)
                wikipedia.set_lang('es')
                respuesta = wikipedia.summary(texto, sentences=1)
                hablar(f'Según Wikipedia:', helena)
                hablar(respuesta, helena)
                continue

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

            elif 'reproduce en youtube' in texto:
                hablar('Reproduciendo en Youtube', helena)
                texto = texto.replace('reproduce en youtube', '')
                pywhatkit.playonyt(texto)
                continue
            
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