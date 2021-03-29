
import speech_recognition as sr
import webbrowser
from gtts import gTTS
import sys
from sys import platform
import os
import subprocess
import time
import playsound
import pyautogui
from pyautogui import press, typewrite, hotkey
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pyttsx3



def speak(text):
    tts = gTTS(text = "I heard" + text, lang = "en", tld = 'ca', slow= False)
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    return 0
def speaker(text):
    tts = gTTS(text = text, lang = "en", tld = 'ca', slow= False)
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


def record_return():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Enter")
        audio = r.listen(source)


        text = r.recognize_google(audio)
        speak(text)
        return text



def type():
    pass

def analysis(text):
    text = text.split()
    #open app
    if "open" in text:
        if ".com" in text[1]:
            website = text[1]
            webbrowser.open_new('https://'+website)
        else:
            if platform == 'darwin':
                for i in range(0, len(text)):
                    if text[i] == "open":
                        app = text[i+1:]
                a = ""
                for i in app:
                    if i != app[len(app)-1]:
                        a += i + ' '
                    else:
                        a+= i
                res=subprocess.run(["open", "/Applications/" + a + ".app"])
                print(res.returncode)
                if res.returncode == 1:
                    tts = gTTS(text = text[1]+ "was not found on this device please try again or find the correct app name", lang = "en", tld = "ca", slow = "False")
                    tts.save("voice.mp3")
                    playsound.playsound("voice.mp3")
                    record()
                else:
                    tts = gTTS(text = "Opening " + a, lang = "en", tld = "ca", slow = "False")
                    tts.save("voice.mp3")
                    playsound.playsound("voice.mp3")
            elif platform == 'win32':
                app = ""
                for i in range(1, len(text)):
                    if text[i] == "open":
                        app == text[i+1:]
                a = ""
                for i in app:
                    if i != app[len(app) - 1]:
                        a += i+ '\ '
                    else:
                        a += i
                x = os.system("start " + text[1])
                print(x)
    elif "tell" in text and "me" in text and "about" in text:
        print("reached")
        l = text.index("about")
        search = ""
        key = ""
        for i in range(l+1, len(text)):
            if i != len(text)-1:
                search += text[i] + "_"
                key += text[i] + " "
            else:
                search += text[i]
                key += text[i]
        print(search)
        link = 'https://en.wikipedia.org/wiki/' + search

        # Specify url of the web page
        source = urlopen(link).read()

        # Make a soup
        soup = BeautifulSoup(source,'lxml')
        soup
        paras = []
        for paragraph in soup.find_all('p'):
            paras.append(str(paragraph.text))
        heads = []
        for head in soup.find_all('span', attrs={'mw-headline'}):
            heads.append(str(head.text))
        text = [val for pair in zip(paras, heads) for val in pair]
        text = ' '.join(text)
        text = re.sub(r"\[.*?\]+", '', text)
        text = text.replace('\n', '')[:-11]
        text = text.split(".")
        l1 = text[0]
        fail = False
        try:
            l1 += text[1]
        except:
            speaker("Could not find any relevant articles. Try other possible keywords please")
            fail = True
        # print(l1)
        if not fail:
            tts = gTTS(text = l1, lang = "en", tld = "ca", slow = "False")
            tts.save("voice.mp3")
            playsound.playsound("voice.mp3")
            speaker("That was what I found for " + key)
            speaker("Would you like to get the transcript?")
            b = record_return()
            if b == "yes":
                print(l1)
            elif b == "no":
                speaker("Ok")
            else:
                speaker("Sorry did not understant that")
    else:
        record()
    record()


def start():
    record()




if __name__ == '__main__':
    allowed = ['darwin', 'win32']
    if platform not in allowed:
        tts = gTTS(text = "This program will not work properly with this system, updates coming soon", lang = "en", tld = "ca", slow = "False")
        tts.save("voice.mp3")
        playsound.playsound("voice.mp3")
        quit()
    start()
