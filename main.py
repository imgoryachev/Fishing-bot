from key import pressButton
from volume import setVolume
from sound import loadSoundDetect
import time

# set volume to 10
setVolume()
# start capturing audio
loadSoundDetect()

while True:
    time.sleep(5)
    pressButton()
    