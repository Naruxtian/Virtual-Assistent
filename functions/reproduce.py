import pywhatkit

def reproduce(rec, talk):
    video = rec.replace('reproduce', '')
    talk('Reproduciendo'+ video)
    pywhatkit.playonyt(video)
