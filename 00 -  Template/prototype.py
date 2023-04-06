import pyautogui as auto
import time
import pywhatkit 

#print(auto.size())
#time.sleep(3)
#print(auto.position())
#time.sleep(3)
#auto.click( 1803, 10, 1, 0,button='left' )
#time.sleep(0.5)
#auto.click( 1803, 10, 1, 0,button='left' )
#time.sleep(0.3)
#auto.press("left")
#pywhatkit.sendwhatmsg('+6282176615694', '_This test message will send at 00.37 AM ! ignore it_', 00, 37, 10)
masukan = input(print("Search : "))
print(masukan)
time.sleep(0.5)
auto.hotkey('win', 'd')

pywhatkit.playonyt(masukan)
pywhatkit.search(masukan)