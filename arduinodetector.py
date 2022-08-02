# i made this for detecting a toggle switch with only two wires. bad code
import serial.tools.list_ports
import requests 
toggle = 0;
while True:
    myports = len([tuple(p) for p in list(serial.tools.list_ports.comports())])
    print (myports)
    if myports == 2:
        if toggle != 1:
            toggle = 1
            r = requests.get(url = "https://example.com/1")
    if myports == 1:
        if toggle != 0:
            toggle = 0
            r = requests.get(url = "https:/example.com/2")
