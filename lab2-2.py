from machine import Pin
import  time

p13 = Pin(13,Pin.OUT)
p14 = Pin(14,Pin.OUT)
p15 = Pin(15,Pin.OUT)
p16 = Pin(16,Pin.OUT)

for i in range(0,...,1): #... คือจำนวนรอบที่ต้องการ
    p13.on()
    time.sleep_ms(100)
    p13.off()
    time.sleep_ms(100)
    
    p14.on()
    time.sleep_ms(100)
    p14.off()
    time.sleep_ms(100)
    
    p15.on()
    time.sleep_ms(100)
    p15.off()
    time.sleep_ms(100)
    
    p16.on()
    time.sleep_ms(100)
    p16.off()
    time.sleep_ms(100)
    
    p15.on()
    time.sleep_ms(100)
    p15.off()
    time.sleep_ms(100)
    
    p14.on()
    time.sleep_ms(100)
    p14.off()
    time.sleep_ms(100)