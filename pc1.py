import serial
import time
from datetime import datetime

import os, shutil
import time

inputMinuteInterval = 1   # max = 1440 m
port = 'COM4'

def findNextTime(inputMinuteInterval) :

        timeNow = str(datetime.now().strftime("%H:%M:%S %p"))
        # print(timeNow)
    
        h = int(timeNow[0:2])
        m = int(timeNow[3:5])
        s = int(timeNow[6:8])
   
        tn = h*3600 + m*60 + s    # time now base Minutes
        nt = tn + inputMinuteInterval * 60
       

        hh  = nt // 3600
        mm = (nt - hh * 3600) // 60 
        ss = nt - (hh * 3600) - mm * 60


        hn = hh - 24 if hh > 24 else hh
        mn = mm - 60 if mm > 60 else mm
        sn = ss - 60 if ss > 60 else ss 

        


        return int(hn), int(mn), int(sn)

def happen(nextTime) :
    
    
    nh, nm, ns = nextTime
    timeNow = str(datetime.now().strftime("%H:%M:%S %p"))
    # print(timeNow)
    
    h = int(timeNow[0:2])
    m = int(timeNow[3:5])
    
    
    if (h == nh) and (m == nm) :
         return True

def getSerialOrNone(port):
    try:
       return serial.Serial(port)
    except:
       
       print("\nWarning:\n       Serial Port Lost  _  PC1")
       return None
    
def pc1():
    
    
    if getSerialOrNone(port) != None :
            
        i = 'pc1'
        serialcomm = serial.Serial('COM4', 9600, timeout=5.0)
        print("pc1 Done")
        time.sleep(2)
        serialcomm.write(i.encode())

   
    
def copy2pc1():

   source      = "H:\Projects\SafeTranferData\Data\Fol_1"
   destination = "H:\Projects\SafeTranferData\Data\Fol_2"

   file_list = os.listdir(source)
   
   print(shutil.copytree(source, destination, dirs_exist_ok=True, ))



nextTime = findNextTime(inputMinuteInterval)
print(nextTime)



while True :
   
   
   if happen(nextTime) :
         
         nextTime = findNextTime(inputMinuteInterval)
         print("nextTime: ", nextTime)
      
     
         

         if getSerialOrNone(port) != None :
              
              copy2pc1()
              pc1()
         
         time.sleep(10)
         
         

        
         
  




"""
serialcomm = serial.Serial('COM4', 9600, timeout=5.0)
while True:
   
         


    i = input("input(pc1 / pc2) :").strip()
    if i =='done':
        print("Finesh program")
        break

    serialcomm.write(i.encode())
    time.sleep(0.5)




    pass

"""

# serialcomm = serial.Serial('COM4', 9600, timeout=5.0)



# while True:
    
#     i = input("input(pc1 / pc2) :").strip()
#     if i =='done':
#         print("Finesh program")
#         break

#     serialcomm.write(i.encode())
#     time.sleep(0.5)
    

# serialcomm.close()