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
ledPowerRed = Pin(26, Pin.OUT)
ledPowerGreen = Pin(27, Pin.OUT)

# Buttons
button1 = Pin(11, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(12, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(13, Pin.IN, Pin.PULL_DOWN)
buttonAddHour = Pin(14, Pin.IN, Pin.PULL_DOWN)

startOfTasksHour = 6
startOfTasksMinute = 0

print("Start: " + str(rtc.datetime()))

task1 = False
task2 = False
task3 = False
dayFinished = False
(year,month,date,day,hour,minute,second,p1)=rtc.datetime()
dayNulled = date - 1
print(dayNulled)

def refreshDay():
    global task1
    global task2
    global task3
    global dayFinished
    
    task1 = False
    task2 = False
    task3 = False
    dayFinished = False

    print("Day refreshed")

def update_leds():
    global dayFinished
    
    ledRed1(task1) # not protoze hardware je blbe
    ledRed2(task2)
    ledRed3(task3)
    
    if task1 and task2 and task3:
        dayFinished = True

    if dayFinished:
        ledPowerRed(0)
        ledPowerGreen(1)
    else:
        ledPowerGreen(0)
        ledPowerRed(1)
    

i = 0

while True:
    (year,month,date,day,hour,minute,second,p1)=rtc.datetime()
        
    i += 1
    if i % 25 == 0:
        print("current time: {}:{}:{}".format(hour,minute,second))
        print("last day of nulling: {}".format(dayNulled))

    update_leds()
    
    if button1.value() == 1 and not task1:
        #ledRed1(1) # vypni
        task1 = True
        print("Task1 splnen")
        
    if button2.value() == 1 and not task2:
        task2 = True
        print("Task2 splnen")
          
    if button3.value() == 1 and not task3:
        task3 = True
        print("Task3 splnen")
            
    if dayNulled != date and (hour > startOfTasksHour or (hour == startOfTasksHour and minute >= startOfTasksMinute)):
        print("refreshing: ", dayNulled != date, hour > startOfTasksHour, hour == startOfTasksHour and startOfTasksMinute >= minute)
        refreshDay()
        dayNulled = date        
        
    time.sleep(0.05)
        
