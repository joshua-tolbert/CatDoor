from machine import Pin
import time
from machine import Pin, UART
import time,utime
from picozero import Speaker
speaker = Speaker(22)
E3=164
F3=174
Gb3=185
G3=196
Ab3=207
A3=220
Bb3=233
B3=246
C4=261
Db4=277
D4=293
Eb4=311
E4=329
F4=349
Gb4=369
G4=392
Ab4=415
A4=440
Bb4=466
B4=493
C5=523
Db5=554
limopen_flag=0
opend=0
sink = 0
motorsync=0
debounce_time=0
data=0
uart = UART(1, baudrate=9600, rx=Pin(5),)#initiate Uart1
uart.init(bits=8, parity=None, stop=1)#8N1 from datasheet
catdata=[]######initialize cat1data variable
data=[]
stuck=0
led = Pin(1, mode=Pin.OUT)
led.value(0)
solmos = Pin(11, mode=Pin.OUT)
motmos = Pin(20, mode=Pin.OUT)
motmos.value(0)
direction= Pin(21, mode=Pin.OUT)
solmos.value(0)
pir1outside = Pin(14, Pin.IN, Pin.PULL_DOWN)
pir2inside = Pin(0, Pin.IN, Pin.PULL_DOWN)
ins = 0
outs=0
ismute=()
note=A4
isclear=1
alarm=F4
with open('catdata','a') as f:#open data from cat1csv stored during sync
    for line in f:
        catdata.extend(eval(line.rstrip('\n').rstrip('\r')))
        
syncbtn= Pin(27, Pin.IN , Pin.PULL_UP)
limopen= Pin(28, Pin.IN , Pin.PULL_UP)
limclose= Pin(15, Pin.IN , Pin.PULL_UP)
alarmbtn=Pin(19, Pin.IN , Pin.PULL_UP)
mutebtn=Pin(26, Pin.IN , Pin.PULL_UP)
def door_open():
    print('door open activated')
    direction.value(0)
    solmos.value(1)
    time.sleep(1)
    motmos.value(1)
    time.sleep(1)

#     if pir1outside.value() == 0 and pir2inside.value() == 0:
#         door_close()
#     if stuck==1:

    





    
   
        
        
# def door_stuck():
#     alarm=F4
#     print('door stuck activated')
#     if alarmbtn.value()==1:
#         speaker.play(alarm)
#         door_open()
#         if alarmbtn.value()==0:
#             print('alarm break')
#             alarm=0
#             door_close()
#          
#             speaker.play(alarm)
#             motmos.value(0)
#             solmos.value(0)
   
  
# def callback(sync):
#     global sync_flag, debounce_time
#     if (time.ticks_ms()-debounce_time) > 500:
#         sync_flag= 1
#         debounce_time=time.ticks_ms()

# syncbtn.irq(trigger=Pin.IRQ_FALLING, handler=callback)
# def fallback(mute):
#     global mute_flag, debounce_time
#     if (time.ticks_ms()-debounce_time) > 500:
#         mute_flag= 1
#         debounce_time=time.ticks_ms()

# mutebtn.irq(trigger=Pin.IRQ_FALLING, handler=fallback)



  # 13 number pin is input
  

            
           # led will turn OFF


while True:
    print(pir2inside.value())
    print(pir1outside.value())
    time.sleep(0.1)
#     if pir1outside.value() == 1:
#         outs= outs+1
#         print('Motion Detected: outside ',outs)
#         time.sleep(5)
#         if outs>0:
#             print('Scanning') #Disable Dormant: Scanning for cat
    if pir2inside.value() == 1:
        ins = ins+1
        print('Motion Detected: inside ',ins)
        time.sleep(5)
        door_open()
    if limopen.value() == 0 and stuck==1:
        motmos.value(0)
        solmos.value(0)
    if limopen.value() == 0 and stuck==0 and sink==1:
        motmos.value(0)
        solmos.value(0)
    if limopen.value() == 0  and stuck==0 and sink==0:
        solmos.value(0)
        motmos.value(0)
            
        
    elif limclose.value()==0:
        motmos.value(0)
        solmos.value(0)
    if pir2inside.value() == 0 and limopen.value() == 0 and pir1outside.value() == 0:
       direction.value(1)
       solmos.value(1)
       time.sleep(1)
       motmos.value(1)
       time.sleep(3)
       if limclose.value()==1:
            print('door stuck')
            speaker.on(F4)
            print('door stuck activated')
            stuck=1
            direction.value(0)
            solmos.value(1)
            time.sleep(1)
            motmos.value(1)
#     if stressbtn.value() is 1:
#        stress_test()
  
        
#     while test is 0:
#         solmos.value(0)
#         motmos.value(0)
#         speaker.play(0)
        
    if stuck == 1:
        led.on()
        time.sleep(0.5)
        led.off()
    if syncbtn.value() is 1 and uart.any() and motorsync is 0:
    
        data =list(uart.read())
        print(len(data))#stores bytes in variable data  
        if len(data)>1:#gets rid of 0x00 reads
            print('the chip is', data)
          
#                 #a=(sum(cat1)-sum(data)) creates a zero condition for cat1 probably not necessary
#                 #b=(sum(cat2)-sum(data))creates a zero condition for cat2 probably not necessary
            if (data) in catdata:#checks if the rfid data maches the data of the stored cat 1
                    print("ACCESS GRANTED")
                    door_open()#indicates if the chip is good. opening door sequence should follow
#                   
            else:
                print('NOT AUTHORIIZED')
                speaker.play(note,10)
# 
    elif syncbtn.value() is 0 and motorsync==0:
        time.sleep(0.1)
        print('sync mode activated')
        sink = 1
        door_open()
        motorsync=1
        
#         syncbtn.value(0)
    elif uart.any() and motorsync==1:
            motorsync=0
            sink=0
            store=list(uart.read())
            if len(store)>1:
                print('the chip stored is', store)
                print(store)
                catdata.append(list(store))
                print(catdata[0])
                file=open("catdata","w")
                file.write(str(catdata))
                file.close()
                direction.value(1)
                solmos.value(1)
                time.sleep(1)
                motmos.value(1)
                time.sleep(3)
                if limclose.value()==1:
                    print('door stuck')
                    speaker.on(F4)
                    print('door stuck activated')
                    stuck=1
                    direction.value(0)
                    solmos.value(1)
                    time.sleep(1)
                    motmos.value(1)
    if mutebtn.value() is 0:
        print("mute Detected")
        ismute=not ismute
        time.sleep(0.5)
        print (ismute)
        if ismute==0:
            note=A4
        elif ismute==1:
            note=0
    if alarmbtn.value() is 0:
        stuck=0
        speaker.off()
        direction.value(1)
        solmos.value(1)
        time.sleep(1)
        motmos.value(1)
        time.sleep(4)
#         if limclose.value()==1:
#             print('door stuck')
#             speaker.play(F4)
#             print('door stuck activated')
#             stuck=1
#     
#             direction.value(0)
#             solmos.value(1)
#             time.sleep(1)
#             motmos.value(1)
#        
# #         
# #         
# #        

