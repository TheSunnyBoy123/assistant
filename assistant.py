
import speech_recognition as sr
from gtts import gTTS
import sys
from sys import platform
import os
import time
import playsound
import pyautogui
from pyautogui import press, typewrite, hotkey


def speak(text):
    tts = gTTS(text = "I heard" + text, lang = "en", tld = 'ca', slow= False)
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
        analysis(text)

def analysis(text):
    text = text.split()
    if "open" in text:
        for i in range(0, len(text)):
            if text[i] == "open":
                app = text[i+1:]
        a = ""
        for i in app:
            if i != app[len(app)-1]:
                a += i + '\ '
            else:
                a+= i
        os.system("open /Applications/" + a + ".app")

def start():
    record()




if __name__ == '__main__':
    allowed = ['darwin']
    if platform not in allowed:
        tts = gTTS(text = "This program will not work properly with this system, updates coming soon", lang = "en", tld = "ca", slow = "False")
        tts.save("voice.mp3")
        playsound.playsound("voice.mp3")
        quit()
    start()
