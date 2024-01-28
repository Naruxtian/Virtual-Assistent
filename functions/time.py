import datetime

def sayTime(talk):
    hora = datetime.datetime.now().strftime('%I:%M %p')
    talk('Son las'+ hora)