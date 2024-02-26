from machine import Pin
import time
from picozero import Speaker
speaker = Speaker(20)
beat = 1
pir1inside = Pin(16, Pin.IN, Pin.PULL_DOWN)
pir2outside = Pin(17, Pin.IN, Pin.PULL_DOWN)
#buzzer = Pin(20, Pin.IN, Pin.PULL_DOWN)
E3=164
db5=554
speaker.play((db5, 1))
speaker.play((E3, 1))



