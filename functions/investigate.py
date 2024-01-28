import wikipedia

def investigate(rec, talk):
    search = rec.replace('investiga', '')
    talk('Investigando'+ search)
    info = wikipedia.summary(search, 1)
    talk(info)