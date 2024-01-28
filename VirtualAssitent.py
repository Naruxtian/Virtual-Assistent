import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

assistent_name = 'Cortana'

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

talk('Hola, soy Cortana, ¿En qué puedo ayudarte?')

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

def run():
    rec = listen()

    

run()