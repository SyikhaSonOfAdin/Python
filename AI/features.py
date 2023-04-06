import datetime
import pyautogui as auto
import time
import os
import pywhatkit as kit
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty('rate',190)
engine.setProperty('volume',1)
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)



nomor = [ '+6282176615694', '+62895376550006', '+62 857-3296-3164', '+62 895-3952-56538', '+62 812-8292-0630', '+62 896-0780-0933' ]
ipan = 0 ; kiraa = 1 ; atmjn = 2 ; umi = 3 ; abi = 4 ; kak_arya = 5

def speak(audio) : 
    engine.say(audio)
    engine.runAndWait()

def whatmsg(nama, pesan, jam, menit) :
    return kit.sendwhatmsg(nomor[nama], pesan, jam, menit, 15, True, 5)
def whatgrupmsg(nama_grup, pesan, jam, menit) :
    return kit.sendwhatmsg_to_group(nama_grup, pesan, jam, menit, 15, True, 5)
def pencarian(judul_pencarian) :
    return kit.search(judul_pencarian)
def youtube(pencarian) :
    return kit.playonyt(pencarian, True, False)
def kirimgambar(nama, image_path, caption) :
    return kit.sendwhats_image( nomor[nama], image_path, caption, 15, True, 5)
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
def word() :
    speak( command )
    os.startfile('C://Program Files//WindowsApps//5319275A.WhatsAppDesktop_2.2228.14.0_x64__cv1g1gvanyjgm//app//Whatsapp.exe') 
    speak(command + "Done")
def closeword() :
    os.system("taskkill /f /im WINWORD.exe")
    speak(command + "Done")
def whatsapp() :
    speak( command )
    os.startfile('C://Program Files//WindowsApps//5319275A.WhatsAppDesktop_2.2228.14.0_x64__cv1g1gvanyjgm//app//Whatsapp.exe') 
    speak(command + "Done")
def closewhatsapp() :
    os.system("taskkill /f /im Whatsapp.exe")
    speak(command + "Done")


r = sr.Recognizer()
while True :

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
        r
        continue

