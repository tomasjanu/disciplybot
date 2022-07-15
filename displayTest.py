from machine import I2C, Pin
from ds1307 import DS1307
import utime
from ssd1306 import SSD1306_I2C
from display import WriteOnLed

i2c_rtc = I2C(0,scl = Pin(1),sda = Pin(0),freq = 100000)
oled = SSD1306_I2C(128, 64, i2c_rtc)

rtc = DS1307(i2c_rtc)


i = 0
while True:
    
    oled.fill(0)
    oled.fill_rect(i, 0, 64, 32, 1)
    oled.show()
    if i==20:
        i-=1
    else:
        i+=1

    (year,month,date,day,hour,minute,second,p1)=rtc.datetime()
    #WriteOnLed(str(hour) + ":" + str(minute) + ":" + str(second))