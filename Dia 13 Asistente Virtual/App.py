import speech_recognition as sr
import pyttsx3
import datetime

from Calendario import Calendario
from MyYoutube import MyYouTube
from MyWikipedia import MyWikipedia
from Calculadora import Calculadora

class App:
    def __init__(self):
        self.sabina = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
        self.helena = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'

        self.client_id = "195351508b814052ae1b1685ef8fcacd"
        self.client_secret = "c3bfe7eb9d76420d88cac90b3134e471"
        self.musica = []
        self.calendario = Calendario()
        self.myyoutube = MyYouTube()
        self.mywikipedia = MyWikipedia()
        self.calculadora = Calculadora()


    def audio_a_texto(self):
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


    def hablar(self, mensaje, voz):
        engine = pyttsx3.init()
        engine.setProperty('voice', voz)
        engine.setProperty('rate', 160)
        engine.say(mensaje)
        engine.runAndWait()


    def saludo(self):
        momento = self.calendario.horaDia()
        mensaje = f'{momento}, Soy Alfa, tu asistente virtual. En que te puedo ayudar'
        self.hablar(mensaje, self.helena)

    def otraPregunta(self):
        otro = True
        while otro:
            texto = self.audio_a_texto().lower()
            if 'sí' in texto:
                return True
            elif 'no' in texto:
                return False

    def main(self):
        inicio = True
        while inicio:
            texto = self.audio_a_texto().lower()
            if 'alfa' in texto:
                texto = texto.replace('alfa', '')

                # Youtube
                if 'abre youtube' in texto:
                    self.hablar('Abriendo Youtube', self.helena)
                    self.myyoutube.openYoutube()
                    continue

                elif 'reproduce en youtube' in texto:
                    texto = texto.replace('reproduce en youtube', '')
                    if texto != ' ':
                        self.hablar('Reproduciendo en Youtube', self.helena)
                        self.myyoutube.play(texto)
                    else:
                        self.hablar('No entendi, Vuelve a intentarlo', self.helena)
                    continue
                
                # Calendario
                elif 'qué hora es' in texto:
                    data = self.calendario.horaActual()
                    self.hablar(data, self.helena)
                    continue
                
                elif 'qué día es hoy' in texto:
                    data = self.calendario.queDiaEsHoy()
                    self.hablar(data, self.helena)
                    self.hablar('Te gustaria saber la hora?', self.helena)
                    data = self.otraPregunta()
                    if data:
                        data = self.calendario.horaActual()
                        self.hablar(data, self.helena)

                # Wikipedia
                elif 'qué es' in texto:
                    self.hablar('Buscando en Wikipedia', self.helena)
                    data = self.mywikipedia.queEs(texto)
                    if data != False:
                        self.hablar(f'Según Wikipedia:', self.helena)
                        self.hablar(data, self.helena)
                    else:
                        self.hablar(f'No consegui nada en Wikipedia sobre: ' + data, self.helena)
                    continue

                elif 'cuánto es' in texto:
                    texto = texto.replace('cuánto es', '')
                    data = self.calculadora.verify(texto)
                    print(f'El resultado es: {data}')
                    self.hablar(f'El resultado es: {data}', self.helena)
                    continue

                elif 'me voy' in texto:
                    self.hablar('Que te vaya bien. Hasta pronto', self.helena)
                    break

                continue

app = App()
app.main()
