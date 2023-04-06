import datetime
import pyttsx3
import speech_recognition as sr
import os
import re
import webbrowser
import subprocess
import wikipedia
import pywhatkit as kit



engine = pyttsx3.init()
engine.setProperty('rate',190)
engine.setProperty('volume',1)
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)

def speak(audio) :
    engine.say(audio)
    engine.runAndWait()
def time() :
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)
def date() :
    year = (datetime.datetime.now().year)
    month = (datetime.datetime.now().month) 
    day = (datetime.datetime.now().day)
    speak(day)
    speak(month)
    speak(year)
def greetings() :
    speak("welcome back sir")
    speak("the current time is")
    time()
    jam = datetime.datetime.now().hour
    if jam >= 1 and jam < 12 :
        speak("Good morining sir ")
    elif jam >= 12 and jam < 18 :
        speak("Good afternoon sir ")
    elif jam >= 18 and jam < 24 :
        speak("Good evening sir ")
        
    
    speak("Jarvis, at your service , please tell me how can i help you")
def myCommand() :

    r = sr.Recognizer()

    with sr.Microphone() as source :
        speak("I am listening ")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try :
        command = r.recognize_google(audio).lower()
        print( command + '\n' )

    except sr.UnknownValueError :
        speak("iam apologize Your last command couldn't be heard sir")
        command = myCommand

    return command  
def assistant(command):
    "if statements for executing commands"

    if 'jarvis' in command:
        speak("Yes sir ?")
        
    elif 'good morning' in command :
        greetings()

    elif 'open whatsapp' in command :
        speak( command )
        os.startfile('C://Program Files//WindowsApps//5319275A.WhatsAppDesktop_2.2228.14.0_x64__cv1g1gvanyjgm//app//Whatsapp.exe') 
        speak(command + "Done")

    elif 'close the whatsapp' in command :
        os.system("taskkill /f /im Whatsapp.exe")
        speak(command + "Done")

    elif 'open game' in command :
        speak( command )
        subprocess.call('D://Program Files (x86)//XBox Game Studios//Worlds Edge//Age of Empires III Definitive Edition//AoE3DE.exe')
        speak("Are you enjoy the geame sir?")

    elif 'open microsoft word' in command :
        speak( command )
        os.startfile('C://Program Files//Microsoft Office//root//Office16//WINWORD.exe')
        speak(command + "Done")

    elif 'close the microsoft word' in command :
        os.system("taskkill /f /im WINWORD.exe")
        speak(command + "Done")

    elif 'show me time' in command :
        time()
        date()

    elif 'open google' in command:
        speak( command )
        speak("sir, what should i search on google")
        cm = myCommand().lower()
        webbrowser.open(f"{cm}")
        
    elif 'where is this' in command:
        speak( command )
        reg_ex = re.search('where (.*)', command)
        url = 'https://www.google.com/maps/@-7.8039211,110.4142924,15z'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        speak(command + "Done")
        
    elif 'open school web' in command:
        speak( command )
        reg_ex = re.search('web (.*)', command)
        url = 'https://ethol.pens.ac.id/mahasiswa/beranda'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        speak(command + "Done")

    elif 'open website' in command:
        speak( command )
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            speak(command + "Done")
        else:
            pass

    elif 'close the google' in command :
        os.system("taskkill /f /im chrome.exe")
        speak(command + "Done")
          
    elif 'thank you' in command:
            speak(" your welcome sir, Happy to help you. Have a good day.")
            print(" :) ")
            exit()

#loop to continue executing multiple commands
while True:
    assistant(myCommand())