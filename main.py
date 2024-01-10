from machine import Pin, UART
import time

uart = UART(1, baudrate=9600, rx=Pin(5),)#initiate Uart1
uart.init(bits=8, parity=None, stop=1)#8N1 from datasheet
data=[ ]#########initialize data variable
cat1data=[]######initialize cat1data variable
cat2data=[]######initialize cat2data variable
with open('cat1.csv','r') as f:#open data from cat1csv stored during sync
    for line in f:
        cat1data.append(line.rstrip('\n').rstrip('\r'))#stores data from cat1csv to cat1 data
        cat1=eval(cat1data[0])#makes cat1data a list of intergers and stores it it cat1 variable
with open('cat2.csv','r') as f:#open data from cat2csv stored during sync
    for line in f:
        cat2data.append(line.rstrip('\n').rstrip('\r'))#stores data from cat2csv to cat2 data
        cat2=eval(cat2data[0])##makes cat2data a list of intergers and stores it it cat2 variable    
interrupt_flag=0
debounce_time=0
pin = Pin(4, Pin.IN, Pin.PULL_UP)
def callback(pin):
    global interrupt_flag, debounce_time
    if (time.ticks_ms()-debounce_time) > 500:
        interrupt_flag= 1
        debounce_time=time.ticks_ms()

pin.irq(trigger=Pin.IRQ_FALLING, handler=callback)
while True:
        
        if interrupt_flag is 0 and uart.any():#checks if there are any bytes on uart1
            data =list(uart.read())#stores bytes in variable data
          
            if len(data)>1:#gets rid of 0x00 reads
                print('the chip is', data)#shows the data on chip 
                #a=(sum(cat1)-sum(data)) creates a zero condition for cat1 probably not necessary
                #b=(sum(cat2)-sum(data))creates a zero condition for cat2 probably not necessary
                if data==cat1:#checks if the rfid data maches the data of the stored cat 1
                    print("ACCESS GRANTED")#indicates if the chip is good. opening door sequence should follow
                elif data==cat2:#checks if the rfid data maches the data of the stored cat 1
                    print("ACCESS GRANTED")#indicates if the chip is good. opening door sequence should follow
                else:
                   print('NOT AUTHORIIZED')#indicates the chip does not match any of the stored cata data
        elif interrupt_flag is 1 and uart.any():
           
            interrupt_flag=0
            store=list(uart.read())
            if len(store)>1:
                print('the chip stored is', store)
                if (cat1)==0:
                    file=open("cat1.csv","w")
                    file.write(str(store))
                    file.close()
                    print('CHIP STORED in cat1')
                    cat1=(store)
                elif (cat2)==0 and (cat1)!=0:
                     
                    file=open("cat2.csv","w")
                    file.write(str(store))
                    file.close()
                    print('CHIP STORED in cat2')
                    cat2=(store)
            
            
             



               
              
     
          
