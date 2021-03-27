
import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound

def speak(text):
    tts = gTTS(text = text, lang = "en", slow= False)
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    return 0

def record():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Enter")
        audio = r.listen(source)


        text = r.recognize_google(audio)
        speak(text)



def start():
    record()


    

if __name__ == '__main__':
    start()
