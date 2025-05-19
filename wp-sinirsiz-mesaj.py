import pyautogui
import time 
import keyboard

time.sleep(10)

def mesaj():
    pyautogui.write("oruspu onur")
    pyautogui.press('enter')

while True:
    if keyboard.is_pressed('q'):
        print("Program durduruldu")
        break
    mesaj()
    time.sleep(0)

