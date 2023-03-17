import pynput
import time
#import threading

from pynput.keyboard import Key, Controller

def pressButton():
    keyboard = Controller()
    keyboard.press(Key.f1)
    keyboard.release(Key.f1)

# pressButton()