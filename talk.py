import speech_recognition as sr
from playsound import playsound
from time import sleep
from datetime import datetime
from draw import *
import webbrowser
import pyttsx3

r = sr.Recognizer()

engine = pyttsx3.init()

def recognize_voice():
    text = ''
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        
        voice = r.listen(source)
        
    try:
        text = r.recognize_google(voice)
        print(text)
    except sr.RequestError:
        speak("Sorry, the I can't access the Google API...")
    except sr.UnknownValueError:
        pass
    return text.lower()

def reply(text_version):
    if 'what is your name' in text_version:
        hi_pic()
        playsound('His_sounds/Name.mp3')
    if 'pikachu good boy' in text_version:
        hi_pic()
        playsound('His_sounds/Pika Happy.mp3')
    if 'pikachu party' in text_version:
        pose_pic()
        playsound('His_sounds/the-pikachu-song.mp3')
    if 'pikachu attack' in text_version:
        attack_pic()
        playsound('His_sounds/pikachu-thunderbolt.mp3')
    if 'pikachu what do you think of eevee' in text_version:
        playsound('His_sounds/Pikachu vs Eevee.mp4')
    if 'pikachu nap' in text_version or 'pikachu sleep' in text_version or 'pikachu tired' in text_version or 'pikachu go to sleep' in text_version:
        exit()
        
    else:
        if 'pikachu' in text_version:
            playsound('His_sounds/pikachu question mark.mp3')

def speak(text):
    engine.say(text)
    engine.runAndWait()
