from machine import Pin
import time
 
pir1inside = Pin(16, Pin.IN, Pin.PULL_DOWN)
pir2outside = Pin(17, Pin.IN, Pin.PULL_DOWN)
n = 0
led = Pin(21, mode = Pin.OUT)
led.value(0)
 
while True:
     if pir1inside.value() == 1:
          n = n+1
          print('Motion Detected: Inside ',n)
          time.sleep(1)
          led.value(1)
          if n>0:
              print('Scanning') #Disable Dormant: Scanning for cat
     elif pir2outside.value() == 1:
          n = n+1
          print('Motion Detected: Outside ',n)
          time.sleep(1)
          led.value(1)
          if n>0:
              print('Scanning')
     else:
         print('Scanning')
         time.sleep(1)
         led.value(0)

     