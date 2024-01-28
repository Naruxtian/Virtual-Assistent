import pyjokes

def tellJoke(talk):
    talk(pyjokes.get_joke(language='es', category='all'))
