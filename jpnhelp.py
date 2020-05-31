import time
import os, random
import board
import digitalio

def rndmp3 ():
    randomfile = random.choice(os.listdir("/home/pi/music/"))
    file = '/home/pi/music/'+ randomfile
    os.system ('omxplayer' + file)                         

button1 = digitalio.DigitalInOut(board.D5)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

button2 = digitalio.DigitalInOut(board.D6)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

while True:
                               if not button1.value:
                                   os.system('omxplayer rndmp3 &')
                               
                               if not button2.value:
                                   os.system('omxplayer rndmp3.play &')
                               
                               time.sleep(.25)
            
print("button pressed")
