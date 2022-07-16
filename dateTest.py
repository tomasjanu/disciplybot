from machine import I2C, Pin
from ds1307 import DS1307
import time

i2c_rtc = I2C(0,scl = Pin(1),sda = Pin(0),freq = 100000)

rtc = DS1307(i2c_rtc)

i = 0
while True:
    
    (year,month,date,day,hour,minute,second,p1)=rtc.datetime()
    print(str(hour) + ":" + str(minute) + ":" + str(second))
    time.sleep(1)
