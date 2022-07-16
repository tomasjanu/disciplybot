from machine import I2C, Pin
from ds1307 import DS1307
import time

# Clock module
i2c_rtc = I2C(0,scl = Pin(1),sda = Pin(0),freq = 100000)
rtc = DS1307(i2c_rtc) 

# LEDs
ledRed1 = Pin(20, Pin.OUT)
ledRed2 = Pin(19, Pin.OUT)
ledRed3 = Pin(18, Pin.OUT)
ledPowerRed = Pin(27, Pin.OUT)
ledPowerGreen = Pin(26, Pin.OUT)

# Buttons
button1 = Pin(11, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(12, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(13, Pin.IN, Pin.PULL_DOWN)
buttonAddHour = Pin(14, Pin.IN, Pin.PULL_DOWN)

task1 = False
task2 = False
task3 = False
dayFinished = False
dayNulled = True
testHours = 4
startOfTasksDay = 6
startOfNulling = 4

print("Start: " + str(rtc.datetime()))

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
    (year,month,date,day,hour,minute,second,p1)=rtc.datetime()

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
        print("Task1 splnen")
        time.sleep(0.5)
        
    if button2.value() == 1:
        ledRed2(1) # vypni
        task2 = True
        print("Task2 splnen")
        time.sleep(0.5)
          
    if button3.value() == 1:
        ledRed3(1) # vypni
        task3 = True
        print("Task3 splnen")
        time.sleep(0.5)
    
    if buttonAddHour.value() == 1:
        if testHours == 24:
            testHours = 1
        testHours+=1
        print("Hours:" + str(testHours))
        time.sleep(0.5)

    if task1 and task2 and task3:
        dayFinished = True

    if dayFinished:
        ledPowerRed(0)
        ledPowerGreen(1)
    else:
        ledPowerGreen(0)
        ledPowerRed(1)

    if hour > startOfTasksDay and not dayNulled:
        refreshDay()

    if hour > startOfNulling and hour < startOfTasksDay and dayNulled:
        dayNulled = False