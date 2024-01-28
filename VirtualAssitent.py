import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

assistent_name = 'Cortana'

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

talk(f"Hola, soy {assistent_name}, ¿En qué puedo ayudarte?")

def listen():
    try:
        with sr.Microphone() as source:
            print('Escuchando...')
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language="es-US")
            rec = rec.lower()
            if assistent_name in rec:
                rec = rec.replace(assistent_name, '')
                print(rec)
    except:
        pass
    return rec

running = True
def run():
    rec = listen()

    if 'reproduce' in rec:
        video = rec.replace('reproduce', '')
        talk('Reproduciendo'+ video)
        pywhatkit.playonyt(video)

    elif 'hora' in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk('Son las'+ hora)

    elif 'investiga' in rec:
        search = rec.replace('investiga', '')
        talk('Investigando'+ search)
        info = wikipedia.summary(search, 1)
        talk(info)
    
    elif 'chiste' in rec:
        talk(pyjokes.get_joke(language='es', category='all'))

    elif 'adios' or 'salir' or 'terminar' in rec:
        talk('Hasta luego')
        exit()

    else:
        talk('No te he entendido, repite por favor')

def exit():
    global running
    running = False

while running:
    run()