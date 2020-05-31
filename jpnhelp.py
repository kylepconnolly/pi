import time
import os, random
import board
import digitalio

def rndmp3 ():
    randomfile = random.choice(os.listdir("/home/pi/Music/"))
    file = ' /home/pi/Music/'+ randomfile
    os.system ('mpg123' + file)
    
def rndmp3 (mp3):
    #mp3=rand
    #rest of mp3 code
    
sig = None
    
print("file")

button1 = digitalio.DigitalInOut(board.D5)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

button2 = digitalio.DigitalInOut(board.D6)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP


while True:
    
    if not button1.value:
        rndmp3(sig)
        print("button pressed")
                               
    if not button2.value:
                               
    time.sleep(.25)
                               



