import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import os
import random
import wikipedia
import webbrowser
import pywhatkit as kit

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():

    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak('Good Morning Sir')
    elif hour>12 and hour<18:
        speak('Good Afternoon Sir')
    else :
        speak('Good Evening Sir')

    speak('How may I Help you?')
    
    
    
    
    
    
    
    
    