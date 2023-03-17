import threading
import time
from pynput.keyboard import Key, Controller, Listener
import keyboard

#button = "f1"

#def on_press(event):
#    print(event.name)

#keyboard.on_press(on_press)
#keyboard.wait('')


#ey_check = keyboard.press_and_release(button)

def run():
    a = 1
    while True:
        print(a)
        time.sleep(1)
        a = a + 1
        keyboard.wait('esc')

run()
            