from machine import Pin
import time
from picozero import Speaker
speaker = Speaker(20)
mutebtn = Pin(18, Pin.IN, Pin.PULL_UP)
led = Pin(21, mode = Pin.OUT)
E3=164
db5=554
L=0
n=0

while True:
    print(n)
    time.sleep(0.2)
    if mutebtn.value() == 0:
        n = n+1
    if n % 2 == 0:
        speaker.play(E3)
    else:
        speaker.play(L)