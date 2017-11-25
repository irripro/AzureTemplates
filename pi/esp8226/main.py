import time
import machine
import ds18x20
import onewire
import socket

dat = machine.Pin(2)
ds = ds18x20.DS18X20(onewire.OneWire(dat))
roms = ds.scan()

#HTML to send to browsers
html = """<!DOCTYPE html>
<html>
<head> <title>ESP8266 LED ON/OFF</title> </head>
<center><h2>A simple webserver for turning HUZZAH Feather LED's on and off with Micropython</h2></center>
<center><h3>(for noobs to both the ESP8266 and Micropython)</h3></center>
<form>
LED0: 
<button name="LED" value="ON0" type="submit">LED ON</button>
<button name="LED" value="OFF0" type="submit">LED OFF</button><br><br>
LED2: 
<button name="LED" value="ON2" type="submit">LED ON</button>
<button name="LED" value="OFF2" type="submit">LED OFF</button>
</form>
</html>
"""

def temperature():
    ds.convert_temp()
    return ds.read_temp(roms[0])
    
#Setup Socket WebServer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
while True:
    response = str(temperature())
    conn, addr = s.accept()
    request = conn.recv(1024)
    conn.send(response)
    conn.close()