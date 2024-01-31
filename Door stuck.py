from machine import Pin, ADC,
import time

# Pin definitions
adc_pin = Pin(26, mode=Pin.IN)
adc = ADC(adc_pin)
from machine import ADC
adc = ADC(0) # Select the ADC_0
from machine import Pin, ADC
adc = ADC(Pin(26, mode=Pin.IN))
print(adc.read_u16())
while True:
    adc_voltage = adc.read_u16() * 3.3 / 65535
    print(adc_voltage)
    time.sleep(1)
    if adc_voltage>1.6:#change the 1.6 via testing
        print('door stuck')