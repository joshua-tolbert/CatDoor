from machine import Pin
import time
syncbtn = Pin(13, Pin.IN, Pin.PULL_UP)
x = 0
#syncbtn.value(0)

while True:
    if x == 0 and syncbtn.value() == 1:
        print('Syncing')
        time.sleep(.5)
    else:
        print ('Chip Synced')
        time.sleep(.5)