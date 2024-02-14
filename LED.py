from machine import Pin, Timer
led = Pin(21, mode = Pin.OUT)
led.value(0)

timer = Timer()

def blink(timer):
    led.toggle()

timer.init(freq=10, mode=Timer.PERIODIC, callback=blink)


