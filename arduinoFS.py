from copyFS import *
from arduinoFS import *
from timeFS import *
from definitionsFS import *

import serial
import time


port = 
def getSerialOrNone(port):

    try:
       return serial.Serial(port)
    except:
       
       print("\nWarning:\n       Serial Port Lost  _  PC1")
       return None
    


def relayPc1():


    if getSerialOrNone(port) != None :
            
        i = 'pc1'
        serialcomm = serial.Serial('COM4', 9600, timeout=5.0)
        print("pc1 Done")
        time.sleep(2)
        serialcomm.write(i.encode())

    