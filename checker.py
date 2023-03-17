import pyaudio
import random
import time
import numpy as np
from key import pressButton
from volume import setVolume
import threading

CHUNK = 1024
THRESHOLD = 75

check = False

def rand():
    i = random.randint(0, 999999)
    return i

def check_bool():
    global check
    global b
    while True:
        if bool(check) == True:
            time.sleep(30)
            if bool(check) == True:
                print("check still True")
                pressButton()
'''
def check_bool():
    global check
    #a = 1
    while True:
        if bool(check) == False:
            a = 1
            print(id(a))
            while bool(check) == False:
                time.sleep(1)

            a = a + 1
            print(a)
            if int(a) == 20:
                print("check still False")
                pressButton()
'''
checker = threading.Thread(target=check_bool)
checker.start()

def loadSoundDetect():
    global check
    # Initialize the Pyaudio object
    p = pyaudio.PyAudio()

    # Open a stream for capturing audio
    stream = p.open(format=pyaudio.paInt16,
                    channels=2,
                    rate=44100,
                    input=True,
                    input_device_index = 1,
                    frames_per_buffer=CHUNK)

    # Start capturing audio
    print("Capturing audio...")
    while True:
        
        # Read audio data from the stream
        data = stream.read(CHUNK)
        data = np.frombuffer(data, dtype=np.int16)
        rms = np.sqrt(np.mean(data**2))
        #print(rms)
        #Check if the RMS exceeds the threshold
        if rms > THRESHOLD:
            print("Loud sound detected!")
            check = True
            pressButton()
            time.sleep(3)
            pressButton()
            check = False
            print(check)

# Close the stream
    stream.stop_stream()
    stream.close()

# Terminate the Pyaudio object
    p.terminate()
time.sleep(5)
setVolume()
pressButton()
loadSoundDetect()









'''
check = False

class CheckVar:
    def __init__(self):
        global check
        self.__check_var = check

    @property
    def check_var(self):
        return self.__check_var

    @check_var.setter
    def check_var(self, value):
        print("Check variable =", value)

checker = CheckVar()
checker.check_var = 10


class CheckVar(threading.Thread):
    def __init__(self, x):
        self._x = x
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self):
        #print("Variable x is changing from {} to {}".format(self._x, value))
        print("check is ", self.x)
        #self._x = value

obj = CheckVar(10)
print(obj.x) # Output: 10

a = 1
while a < 21:
    print(a)
    a = a+1
    time.sleep(1)
    
    #if obj.x == a:
    #    print("obj is 10")
    #    check = True
    
    if check == True:
        break   


def changeCheck():
    global check
    print(check)
    s = 0
    while s < 10:
        s = s + 1
        time.sleep(1)
        print("s = ", s)
        if int(s) == 5:
            check = True
        #print(check)

def inc():
    global check
    x = 1
    while int(x) <= 20:
        print(x)
        x = x + 1
        time.sleep(1)
        if check == True:
            break

inc_thread = threading.Thread(target=inc)
start_check = threading.Thread(target=changeCheck)
inc_thread.start()
start_check.start()
'''