while True :

#     with sr.Microphone() as source :
#         speak("I am listening ")
#         r.pause_threshold = 1
#         r.adjust_for_ambient_noise(source, duration=1)
#         audio = r.listen(source)

#     try :
#         command = r.recognize_google(audio).lower()
#         print( command + '\n' )

#     except sr.UnknownValueError :
#         speak("iam apologize Your last command couldn't be heard sir")
#         r
#         continue