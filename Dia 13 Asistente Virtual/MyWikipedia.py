import wikipedia

class MyWikipedia:

    def __init__(self):
        pass
    
    def queEs(self,texto):
        wikipedia.set_lang('es')
        respuesta = wikipedia.summary(texto, sentences=1)
        if respuesta:
            return respuesta
        else:
            return False