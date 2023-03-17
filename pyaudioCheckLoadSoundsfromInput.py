import pyaudio
import numpy as np

# Define the chunk size and sample rate
#CHUNK = 1024
CHUNK = 1024
RATE = 44100

# Define the loudness threshold
THRESHOLD = 60

# Initialize the Pyaudio object
p = pyaudio.PyAudio()

# Open a stream for capturing audio
stream = p.open(format=pyaudio.paInt16,
                channels=2,
                rate=RATE,
                input=True,
                input_device_index = 1,
                frames_per_buffer=CHUNK)

# Start capturing audio
print("Capturing audio...")
while True:
    # Read audio data from the stream
    data = stream.read(CHUNK)

    # Convert the audio data from string to numpy array
    data = np.frombuffer(data, dtype=np.int16)
    #print(data)
    # Calculate the RMS of the audio data
    rms = np.sqrt(np.mean(data**2))
    #print(rms)
    # Check if the RMS exceeds the threshold
    if rms > THRESHOLD:
        print("Loud sound detected!")

    # Do some other processing here

# Close the stream
stream.stop_stream()
stream.close()

# Terminate the Pyaudio object
p.terminate()