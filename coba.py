# import turtle
# import time
# #creating a square with turtle
# t = turtle.Turtle()
# t.forward(100)
# time.sleep(3)
# t.color('blue')
# time.sleep(3)
# t.right(90)
# time.sleep(3)
# t.forward(100)
# time.sleep(3)
# t.right(90)
# time.sleep(3)
# t.forward(100)
# time.sleep(3)
# t.right(90)
# time.sleep(3)
# t.forward(100)
import pyttsx3

engine = pyttsx3.init()

for voice in engine.getProperty('voices'):
    print(voice)