from machine import Pin
import time
 
ledRed1 = Pin(20, Pin.OUT)
ledRed2 = Pin(19, Pin.OUT)
ledRed3 = Pin(18, Pin.OUT)
ledPowerRed = Pin(27, Pin.OUT)
ledPowerGreen = Pin(26, Pin.OUT)

button1 = Pin(11, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(12, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(13, Pin.IN, Pin.PULL_DOWN)
buttonAddHour = Pin(14, Pin.IN, Pin.PULL_DOWN)

task1 = False
task2 = False
task3 = False
dayFinished = False
dayNulled = True
hours = 4

print("Start. Hours: " + str(hours))

def refreshDay():
    global task1
    global task2
    global task3
    global dayFinished
    global dayNulled

    task1 = False
    task2 = False
    task3 = False

    dayFinished = False
    dayNulled = True

    print("Day refreshed")
    time.sleep(0.5)

while True:
    if(dayFinished == False):
        if not task1:
            ledRed1(0) #zapni
        if not task2:
            ledRed2(0) #zapni
        if not task3:        
            ledRed3(0) #zapni
        
    if button1.value() == 1:
        ledRed1(1) # vypni
        task1 = True
        print("ButtonRed zmacknut")
        time.sleep(0.5)
        
    if button2.value() == 1:
        ledRed2(1) # vypni
        task2 = True
        print("ButtonGreen zmacknut")
        time.sleep(0.5)
          
    if button3.value() == 1:
        ledRed3(1) # vypni
        task3 = True
        print("ButtonWhite zmacknut")
        time.sleep(0.5)
    
    if buttonAddHour.value() == 1:
        if hours == 24:
            hours = 1
        hours+=1
        print("Hours:" + str(hours))
        time.sleep(0.5)

    if task1 and task2 and task3:
        dayFinished = True

    if dayFinished:
        ledPowerRed(0)
        ledPowerGreen(1)
    else:
        ledPowerGreen(0)
        ledPowerRed(1)

    if hours > 6 and not dayNulled:
        refreshDay()

    if hours > 4 and hours < 6 and dayNulled:
        dayNulled = False