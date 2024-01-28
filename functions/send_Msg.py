import pywhatkit
import speech_recognition as sr
import json


def send_message(rec, talk):
    contact = select_contact()
    msg = write_message(talk)
    pywhatkit.sendwhatmsg_instantly(contact, msg)

def select_contact(talk):
    talk("¿A quién quieres enviar el mensaje?")
    listener = sr.Recognizer()

    contact_selected = False
    

    with open('contacts.json') as f:
        contacts = json.load(f)
    try:
        with sr.Microphone() as source:
            print('Escuchando contacto...')
            voice = listener.listen(source)
            contact = ""
            contact = listener.recognize_google(voice, language="es-ES").lower()
    except:
        pass

    
    for person in contacts:
        if person['name'] in contact:
            number = person['number']
            break

    return contact

def write_message(talk):
    talk("¿Qué mensaje quieres enviar?")
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print('Escuchando mensaje...')
            voice = listener.listen(source)
            msg = ""
            msg = listener.recognize_google(voice, language="es-ES").lower()
    except:
        pass
    return msg
   

