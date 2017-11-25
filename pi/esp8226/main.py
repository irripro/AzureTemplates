import time
import machine
import ds18x20
import onewire
import socket

dat = machine.Pin(2)
ds = ds18x20.DS18X20(onewire.OneWire(dat))
roms = ds.scan()

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