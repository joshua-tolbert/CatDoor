from machine import Pin
import time
limopen= Pin(12, Pin.IN , Pin.PULL_DOWN)
limclose= Pin(11, Pin.IN , Pin.PULL_DOWN)
motmos = Pin(27, mode=Pin.OUT)
direction = Pin(26, mode=Pin.OUT)
motmos.value(1)
direction.value(0)
openbtn= Pin(18, Pin.IN , Pin.PULL_UP)
closebtn=Pin(13, Pin.IN , Pin.PULL_UP)
while True:
    if openbtn.value()==0:
        direction.value(0)
        motmos.value(1)
    if limopen.value()==0:
        print('lim reach')
        motmos.value(0)
    if closebtn.value()==0:
        direction.value(1)
        motmos.value(1)
    if limclose.value()==0:
        print('lim reach')
        motmos.value(0)
    
        
       
 
    time.sleep(0.1)