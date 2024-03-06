from machine import Pin, ADC,
import time
limopen= Pin(12, Pin.IN , Pin.PULL_DOWN)
limclose= Pin(11, Pin.IN , Pin.PULL_DOWN)
motmos = Pin(27, mode=Pin.OUT)
openbtn= Pin(18, Pin.IN , Pin.PULL_UP)
closebtn=Pin(13, Pin.IN , Pin.PULL_UP)
motmos = Pin(27, mode=Pin.OUT)
direction = Pin(26, mode=Pin.OUT)
direction.value(1)

motmos.value(1)
# Pin definitions
adc_pin = Pin(28, mode=Pin.IN)
adc = ADC(adc_pin)
from machine import ADC
adc = ADC(2) # Select the ADC_0
from machine import Pin, ADC
adc = ADC(Pin(28, mode=Pin.IN))
# print(adc.read_u16())
# time.sleep(1)
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
    
        
    
    adc_voltage = adc.read_u16()*3.3/65535
    time.sleep(1)
    print(adc_voltage)
    

    if adc_voltage>0.022:#change the 1.6 via testing
        print('door stuck')
    else:
        print('NOP')