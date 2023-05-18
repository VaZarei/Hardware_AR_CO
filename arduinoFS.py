from copyFS import *
from arduinoFS import *
from timeFS import *
from definitionsFS import *

import serial
import time
import os




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


def check_flash(flash_address):

    i = 0
    try:
      
      for files in os.listdir(flash_address) :
        i+=1
      if i > 0 :
         print("\nFlash staus: OK !")
         return True

    except FileNotFoundError :
       
       print("\nFlash staus: FAIL !")
       return False


def cleanFlash(flash_address):
     
     os.system(f"rd /s /q {flash_address}")
     