import sys
import pyttsx3
import speech_recognition as sr
from features import *





def myCommand() :

    r = sr.Recognizer()

    with sr.Microphone() as source :
        speak("I am listening ")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try :
        command = r.recognize_google(audio, language="id-ID").slower()
        print( command + '\n' )

    except sr.UnknownValueError :
        speak("iam apologize Your last command couldn't be heard sir")
        command = myCommand
        
    return command

     


def task_execution() :
    if 'Hello' in command or 'Hallo' in command :
        greetings()
    elif 'open whatsapp' in command :
        whatsapp()
        


if 'sleep' in command :
    speak("Ok Sir")
    while True :
        if 'wake up' in command :
            task_execution()
        elif 'goodbye' in command :
            speak("Thankyou sir, have a good day!")
            sys.exit()
            

        