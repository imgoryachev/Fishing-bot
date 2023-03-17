import pyaudio
import time
import numpy as np
from key import pressButton
from volume import setVolume

CHUNK = 1024
THRESHOLD = 75
def loadSoundDetect():

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
            pressButton()
            time.sleep(3)
            pressButton()

# Close the stream
    stream.stop_stream()
    stream.close()

# Terminate the Pyaudio object
    p.terminate()
time.sleep(5)
setVolume()
pressButton()
loadSoundDetect()