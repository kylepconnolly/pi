import time
import os, random
import board
import digitalio

def rndmp3 ():
    randomfile = random.choice(os.listdir("/home/pi/Music/"))
    file = ' /home/pi/Music/'+ randomfile
    os.system ('mpg123' + file)
    return file
    
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
        sig = rndmp3()
        print("button 1 pressed")
                               
    if not button2.value:
        os.system ('mpg123' + sig)
        print("button 2 pressed")
                               
    time.sleep(.25)
                               
