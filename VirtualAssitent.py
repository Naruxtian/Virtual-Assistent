import speech_recognition as sr
import pyttsx3
import pyjokes
from functions.reproduce import reproduce
from functions.time import sayTime
from functions.investigate import investigate
from functions.joke import tellJoke

assistent_name = 'pal'

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    listener = sr.Recognizer()
    status = False
    try:
        with sr.Microphone() as source:
            print('Escuchando...')
            # listener.adjust_for_ambient_noise(source, duration=1)
            voice = listener.listen(source)
            rec = ""
            rec = listener.recognize_google(voice, language="es-ES").lower()

            if assistent_name in rec:
                rec = rec.replace(f"{assistent_name} ", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                status = True
            else:
                status = False
                print("Esperando ordenes...")
    except:
        pass
    return {'order':rec, 'status':status}

running = True
talk(f"Hola, soy {assistent_name}, ¿En qué puedo ayudarte?")
def run():
    rec_data = listen()

    rec = rec_data['order']
    status = rec_data['status']

    if status:
        if 'estas ahi' in rec:
            talk('Estoy a tu servicio')

        elif 'reproduce' in rec:
            reproduce(rec, talk)

        elif 'hora' in rec:
            sayTime(talk)

        elif 'investiga' in rec:
            investigate(rec, talk) 
        
        elif 'chiste' in rec:
            tellJoke(talk)

        elif 'adios' or 'terminar' in rec:
            talk('Hasta luego')
            exit()

        else:
            talk('No te he entendido, repite por favor')

def exit():
    global running
    running = False

while running:
    run()