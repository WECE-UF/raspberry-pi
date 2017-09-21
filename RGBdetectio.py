#working
import time
import RPi.GPIO as IO
IO.setmode (IO.BCM)
IO.setwarnings(False)  #do not show any warnings
x=0
IO.setup(6,IO.OUT      #pins 6,5,… are set as output
IO.setup(5,IO.OUT)
IO.setup(27,IO.OUT)
IO.setup(17,IO.OUT)
IO.setup(13,IO.OUT)
IO.setup(22,IO.OUT)
IO.setup(26,IO.OUT)
IO.setup(21,IO.IN)     #pins 21,20… are set as input
IO.setup(20,IO.IN)
IO.setup(16,IO.IN)
IO.setup(12,IO.IN)
IO.setup(25,IO.IN)
IO.setup(24,IO.IN)
IO.setup(23,IO.IN)
IO.setup(18,IO.IN)
while 1:
    IO.output(6,0)     #choose red array by putting S2 and S3 low
    IO.output(5,0)
    time.sleep(0.1)
    IO.output(26,1)    #reset counter one time
    time.sleep(0.2)
    IO.output(26,0)
    IO.output(22,0)    #enable output of module for 100msec for counter to read frequency
    time.sleep(0.01)
    IO.output(22,1)
    if(IO.input(21)==True):
        x=1
    if(IO.input(20)==True):
        x=x+2
    if(IO.input(16)==True):
        x=x+4
    if(IO.input(12)==True):
        x=x+8
    if(IO.input(25)==True):
        x=x+16
    if(IO.input(24)==True):
        x=x+32
    if(IO.input(23)==True):
        x=x+64
    if(IO.input(18)==True):
        x=x+128
    print("Red=")     #detect value counted by counter
    R = x-50
    print(R)
    x=0
    
    IO.output(6,0)    #choose blue array
    IO.output(5,1)
    time.sleep(0.1)
    IO.output(26,1)   #reset counter one time
    time.sleep(0.2)
    IO.output(26,0)
    IO.output(22,0)   #enable output of module for 100msec for counter to read frequency
    time.sleep(0.01)
    IO.output(22,1)
    if(IO.input(21)==True):
        x=1
    if(IO.input(20)==True):
        x=x+2
    if(IO.input(16)==True):
        x=x+4
    if(IO.input(12)==True):
        x=x+8
    if(IO.input(25)==True):
        x=x+16
    if(IO.input(24)==True):
        x=x+32
    if(IO.input(23)==True):
        x=x+64
    if(IO.input(18)==True):
        x=x+128
    print("Blue=")    #detect value counted by counter
    B = x-20
    print(B)
    x=0
    
    IO.output(6,1)    #choose green array
    IO.output(5,1)
    time.sleep(0.1)
    IO.output(26,1)   #reset counter one time
    time.sleep(0.2)
    IO.output(26,0) 
    IO.output(22,0)   #enable output of module for 100msec for counter to read frequency
    time.sleep(0.01)
    IO.output(22,1)
    if(IO.input(21)==True):
        x=1
    if(IO.input(20)==True):
        x=x+2
    if(IO.input(16)==True):
        x=x+4
    if(IO.input(12)==True):
        x=x+8
    if(IO.input(25)==True):
        x=x+16
    if(IO.input(24)==True):
        x=x+32
    if(IO.input(23)==True):
        x=x+64
    if(IO.input(18)==True):
        x=x+128
    print("Green=")   #detect value counted by counter
    G=x-42
    print(G)
    x=0
    print
    print
    print
    print
    print
    print
    if((R>=B+10)and(R>=G+10)):    #if RED color intensity is high light RED led
        IO.output(17,0)
    elif((G>=B+10)and(G>=R+10)):  #if GREEN color intensity is high light GREEN led
        IO.output(13,0)
    elif((B>=R+10)and(B>=G+10)):  #if BLUE color intensity is high light BLUE led
        IO.output(27,0)
    
    
    time.sleep(2)    #after 2 sec turn off LEDs
    IO.output(17,1)
    IO.output(13,1)
    IO.output(27,1)