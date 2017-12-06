import time
import machine
import ds18x20
import onewire
import socket
from machine import Pin
from umqtt.simple import MQTTClient

dat = machine.Pin(5)
ds = ds18x20.DS18X20(onewire.OneWire(dat))
roms = ds.scan()
relay = Pin(0,Pin.OUT)

def temperature():
    ds.convert_temp()
    return ((ds.read_temp(roms[0]) * 1.8) + 32)

rtc = machine.RTC()
rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

# set RTC.ALARM0 to fire after 10 seconds (waking the device)
rtc.alarm(rtc.ALARM0, 60000)

def sendmsg(server="10.0.0.160"):
    msg = str("%s:%s" %(utime.localtime(),temperature()))
    c = MQTTClient("umqtt_client", server)
    c.connect()
    c.publish(b"sensor/temperature", b"{}".format(temperature())
    c.disconnect()

sendmsg()
# put the device to sleep
machine.deepsleep()

'''   
#Setup Socket WebServer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
while True:
    response = str(temperature())
    time.sleep_ms(750)
    conn, addr = s.accept()
    request = conn.recv(1024)
    conn.send(response)
    conn.close() 
'''