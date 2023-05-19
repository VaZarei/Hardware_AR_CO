from copyFS import *
from arduinoFS import *
from timeFS import *
from definitionsFS import *

import serial
import time
import os
import subprocess





def getSerialOrNone(port):

    try:
       return serial.Serial(port)
    except:
       
       print("\nWarning:\n       Serial Port Lost  _  PC1")
       return None
 

def relayPc1():


    if getSerialOrNone(comPort) != None :
            
        i = 'pc1'
        serialcomm = serial.Serial('COM4', 9600, timeout=5.0)
        print("pc1 Done")
        time.sleep(2)
        serialcomm.write(i.encode())

# may be no need to use
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


def findUsbLetter(usbName):

    DeviceID   = []
    VolumeName = []

    output = subprocess.check_output("powershell Get-WmiObject -Class Win32_LogicalDisk", shell=True)
    
    m = (output.decode())
    mm = m.splitlines()

    for i in mm :
      if i[0:8] == "DeviceID"  :
        
            ID = i[15:]
            DeviceID.append(ID)
            
      if i[0:10] == "VolumeName" :
            VN = i[15:]
            if VN == '' :
                    
                    VolumeName.append("None")
            else:

                    VolumeName.append(VN)
                

    for index , volumeN in enumerate(VolumeName) :
       
        if volumeN.lower() == str(usbName.lower()) :
           return str(DeviceID[index])

    return "None"

    
def cleanFlash(flash_address):
     
     os.system(f"rd /s /q {flash_address}")
     