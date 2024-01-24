from machine import Pin
import time
 
pir = Pin(22, Pin.IN, Pin.PULL_DOWN)
n = 0
 
while True:
     if pir.value() == 1:
          n = n+1
          print('Motion Detected ',n)
          time.sleep(4)
          if n>0:
              print('disable dormant: scanning for cat')
     else:
         print('fuqq off')
         time.sleep(1)