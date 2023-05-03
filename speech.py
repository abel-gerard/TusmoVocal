import speech_recognition as sr
from unidecode import unidecode

def getAudio(recognizer, source):
    recognizer.adjust_for_ambient_noise(source, duration=1)
    audio = recognizer.listen(source, phrase_time_limit=3)
    
    return audio

def detect():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Mot :")
        audio = getAudio(recognizer, source)

    try:
        text = recognizer.recognize_google(audio, language="fr-FR")
        return text
    except sr.UnknownValueError or sr.RequestError:
        print("Error")
        
    return ""
        
def clean(text):
    cleanTextArray = list(map(lambda word: unidecode(word), text.strip().upper().split()))
    
    return cleanTextArray
