# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
import webrepl
import ntptime
import time
import utime
import machine
import ds18x20
import onewire
import socket
from machine import Pin
from umqtt.simple import MQTTClient

webrepl.start()
gc.collect()

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('QAZHOME2G', 'adamhussain')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
   
do_connect()
time.sleep_ms(5000)
ntptime.settime()


dat = machine.Pin(5)
ds = ds18x20.DS18X20(onewire.OneWire(dat))
roms = ds.scan()
relay = Pin(0,Pin.OUT)

def temperature():
    ds.convert_temp()
    return ((ds.read_temp(roms[0]) * 1.8) + 32)

def sendmsg(server="10.0.0.160"):
    msg = str("%s:%s" %(utime.localtime(),temperature()))
    c = MQTTClient("umqtt_client", server)
    c.connect()
    c.publish(b"sensor/temperature", b"{}".format(temperature())
    c.disconnect()

rtc = machine.RTC()
rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

# set RTC.ALARM0 to fire after 10 seconds (waking the device)
rtc.alarm(rtc.ALARM0, 60000)

sendmsg()
# put the device to sleep
#machine.deepsleep()